#!/usr/bin/env python3
"""No-inference regression checks for sanitized inventory and diagnostic isolation."""
import ast
import json
from pathlib import Path
import subprocess
import sys
import tempfile
from types import SimpleNamespace
import unittest
from unittest.mock import patch

import hardware_inventory

ROOT = Path(__file__).resolve().parents[1]


class HardwareDiagnosticTests(unittest.TestCase):
    def test_nvidia_directory_is_not_a_gpu_device_node(self):
        directory = SimpleNamespace(is_char_device=lambda: False)
        with patch.object(hardware_inventory, "command", return_value=(9, "")), \
             patch.object(hardware_inventory, "nvidia_pci_devices", return_value=[]), \
             patch.object(hardware_inventory.Path, "glob", return_value=[directory]):
            result = hardware_inventory.inventory(str(ROOT))
        self.assertTrue(result["gpu"]["nvidia_matching_paths_present"])
        self.assertFalse(result["gpu"]["nvidia_device_nodes_present"])

    def test_inventory_omits_identity_and_environment_values(self):
        private = "private-host-identity-and-credential"
        cpu = json.dumps({"lscpu": [
            {"field": "Model name:", "data": "Synthetic CPU"},
            {"field": "Hostname:", "data": private},
        ]})

        def fake_command(args):
            return (0, cpu) if args[0] == "lscpu" else (9, "")

        with patch.object(hardware_inventory, "command", side_effect=fake_command), \
             patch.object(hardware_inventory, "nvidia_pci_devices", return_value=[]), \
             patch.dict("os.environ", {"SSH_CONNECTION": private, "API_KEY": private}), \
             patch.object(hardware_inventory.shutil, "which", return_value="/private/bin/tool"):
            result = hardware_inventory.inventory(str(ROOT))
        encoded = json.dumps(result)
        self.assertNotIn(private, encoded)
        self.assertNotIn("/private/", encoded)
        self.assertTrue(result["context"]["ssh_environment_present"])
        self.assertEqual(result["cpu"]["Model name"], "Synthetic CPU")
        self.assertEqual(result["gpu"]["nvidia_query_status"], "unavailable_or_failed")

    def test_failed_smi_with_pci_hardware_is_scoped_inaccessibility(self):
        pci = [{'vendor': 'NVIDIA', 'device_id': '0x20b0', 'class': '0x030200', 'driver': 'nvidia'}]
        with patch.object(hardware_inventory, 'command', return_value=(9, '')), \
             patch.object(hardware_inventory, 'nvidia_pci_devices', return_value=pci):
            result = hardware_inventory.inventory(str(ROOT), 'sandbox')
        self.assertEqual(result['observation_scope'], 'sandbox')
        self.assertEqual(result['gpu']['nvidia_query_status'], 'inaccessible_in_this_execution_scope')
        self.assertEqual(result['gpu']['nvidia_pci_devices'], pci)

    def test_successful_outside_query_reports_gpu_memory(self):
        def fake(args):
            return (0, 'NVIDIA A100-SXM4-40GB, 40960, 40018, 580.178.04, 55, 400, 35, 0') if args[0] == 'nvidia-smi' else (9, '')
        with patch.object(hardware_inventory, 'command', side_effect=fake), \
             patch.object(hardware_inventory, 'nvidia_pci_devices', return_value=[]):
            result = hardware_inventory.inventory(str(ROOT), 'outside-sandbox')
        self.assertEqual(result['gpu']['nvidia_query_status'], 'success')
        self.assertEqual(result['gpu']['nvidia_gpus'][0]['memory.total'], '40960')
        self.assertEqual(result['gpu']['nvidia_gpus'][0]['memory.free'], '40018')

    def test_inventory_never_overwrites_observation(self):
        with tempfile.TemporaryDirectory() as directory:
            target = Path(directory) / "inventory.json"
            target.write_text("prior observation")
            with patch.object(sys, "argv", ["hardware_inventory.py", "--output", str(target)]), \
                 patch.object(hardware_inventory, "inventory", return_value={}):
                with self.assertRaises(FileExistsError):
                    hardware_inventory.main()
            self.assertEqual(target.read_text(), "prior observation")

    def test_diagnostic_outputs_cannot_target_study_directory(self):
        result = subprocess.run([
            sys.executable, str(ROOT / "scripts/local_feasibility_benchmark.py"),
            "--model", "Qwen/Qwen3.5-2B", "--revision", "unused",
            "--output", str(ROOT / "data/outputs/diagnostic-should-not-exist.jsonl")],
            capture_output=True, text=True)
        self.assertEqual(result.returncode, 2)
        self.assertIn("diagnostic output must be below ignored project .local/", result.stderr)
        self.assertFalse((ROOT / "data/outputs/diagnostic-should-not-exist.jsonl").exists())

    def test_committed_prompt_provenance_matches_current_diagnostics(self):
        source = (ROOT / "scripts/local_feasibility_benchmark.py").read_text()
        tree = ast.parse(source)
        prompts = next(ast.literal_eval(node.value) for node in tree.body
                       if isinstance(node, ast.Assign)
                       and any(isinstance(target, ast.Name) and target.id == "DIAGNOSTICS"
                               for target in node.targets))
        provenance = json.loads((ROOT / "data/evaluation/amendments/prelim-157-four-model-0.2/DIAGNOSTIC_PROMPTS.json").read_text())
        self.assertEqual(set(prompts), {"en", "bn", "bn_cs"})
        stored = provenance["versions"]["synthetic-backup-0.2"]["prompts"]
        self.assertEqual(prompts, {key: value["text"] for key, value in stored.items()})
        self.assertEqual(len(set(prompts.values())), 3)


if __name__ == "__main__":
    unittest.main()
