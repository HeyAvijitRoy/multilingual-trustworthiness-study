#!/usr/bin/env python3
"""Emit a sanitized, read-only Linux inference-host inventory as JSON.

No network requests, model loads, environment dumps, hostnames, serial numbers,
usernames, process command lines, or absolute cache paths are collected. Run with
the Python environment intended for inference: package versions are interpreter
specific. Unsupported observations are null rather than inferred hardware.
"""
from __future__ import annotations

import argparse
import csv
from datetime import datetime, timezone
import importlib.metadata
import json
import os
from pathlib import Path
import platform
import shutil
import subprocess


def read(path: str) -> str | None:
    try:
        return Path(path).read_text().strip()
    except (OSError, UnicodeError):
        return None


def command(args: list[str]) -> tuple[int | None, str]:
    try:
        result = subprocess.run(args, capture_output=True, text=True, timeout=15)
        return result.returncode, result.stdout.strip()
    except (OSError, subprocess.TimeoutExpired):
        return None, ""


def version(package: str) -> str | None:
    try:
        return importlib.metadata.version(package)
    except importlib.metadata.PackageNotFoundError:
        return None


def nvidia_pci_devices() -> list[dict]:
    """PCI visibility can establish hardware presence when /dev is sandboxed."""
    devices = []
    for device in Path('/sys/bus/pci/devices').glob('*'):
        if read(str(device / 'vendor')) != '0x10de':
            continue
        driver = device / 'driver'
        devices.append({'vendor': 'NVIDIA', 'device_id': read(str(device / 'device')),
                        'class': read(str(device / 'class')),
                        'driver': driver.resolve().name if driver.exists() else None})
    return sorted(devices, key=lambda d: (d['device_id'] or '', d['class'] or ''))


def inventory(disk_path: str = ".", execution_scope: str = "unspecified") -> dict:
    cpu = {}
    rc, out = command(["lscpu", "--json"])
    if rc == 0:
        fields = {row["field"].rstrip(":"): row["data"]
                  for row in json.loads(out)["lscpu"]}
        for name in ("Architecture", "Vendor ID", "Model name", "CPU(s)",
                     "Thread(s) per core", "Core(s) per socket", "Socket(s)",
                     "Hypervisor vendor", "Virtualization type", "Flags"):
            cpu[name] = fields.get(name)
    mem = {}
    for line in (read("/proc/meminfo") or "").splitlines():
        key, value = line.split(":", 1)
        if key in {"MemTotal", "MemAvailable", "SwapTotal", "SwapFree"}:
            mem[key + "_bytes"] = int(value.split()[0]) * 1024
    gpu_fields = ["name", "memory.total", "memory.free", "driver_version",
                  "power.draw", "power.limit", "temperature.gpu", "utilization.gpu"]
    gpu_rc, gpu_out = command([
        "nvidia-smi", "--query-gpu=" + ",".join(gpu_fields),
        "--format=csv,noheader,nounits"])
    gpus = []
    if gpu_rc == 0:
        for row in csv.reader(gpu_out.splitlines()):
            if len(row) == len(gpu_fields):
                gpus.append(dict(zip(gpu_fields, (value.strip() for value in row))))
    disk = shutil.disk_usage(disk_path)
    nvidia_paths = list(Path("/dev").glob("nvidia*"))
    pci_devices = nvidia_pci_devices()
    release = read("/proc/sys/kernel/osrelease") or ""
    cgroup = {}
    for name in ("cpu.max", "memory.max", "memory.current", "cpuset.cpus.effective"):
        cgroup[name] = read("/sys/fs/cgroup/" + name)
    return {
        "schema_version": "sanitized-hardware-0.1",
        "observed_at_utc": datetime.now(timezone.utc).isoformat(),
        "observation_scope": execution_scope,
        "os": {"system": platform.system(), "release": platform.release(),
               "architecture": platform.machine()},
        "context": {
            "wsl_detected": "microsoft" in release.lower(),
            "container_marker_detected": Path("/.dockerenv").exists()
                or Path("/run/.containerenv").exists(),
            "ssh_environment_present": bool(os.environ.get("SSH_CONNECTION")),
            "remote_vscode_environment_present": bool(os.environ.get("VSCODE_IPC_HOOK_CLI")),
            "note": "Absence of markers does not prove native or unshared execution.",
        },
        "cpu": cpu,
        "cpu_affinity_count": len(os.sched_getaffinity(0))
            if hasattr(os, "sched_getaffinity") else os.cpu_count(),
        "load_average": list(os.getloadavg()) if hasattr(os, "getloadavg") else None,
        "memory": mem,
        "cgroup_v2_root_observations": cgroup,
        "gpu": {
            "nvidia_smi_command_present": shutil.which("nvidia-smi") is not None,
            "nvidia_smi_exit_code": gpu_rc,
            "nvidia_query_status": ("success" if gpu_rc == 0 else
                                    "inaccessible_in_this_execution_scope" if pci_devices else
                                    "unavailable_or_failed"),
            "nvidia_gpus": gpus,
            "nvidia_pci_devices": pci_devices,
            "nvidia_driver_module_present": Path('/sys/module/nvidia').exists(),
            "nvidia_matching_paths_present": bool(nvidia_paths),
            "nvidia_device_nodes_present": any(p.is_char_device() for p in nvidia_paths),
            "dri_directory_present": Path("/dev/dri").is_dir(),
            "rocm_smi_command_present": shutil.which("rocm-smi") is not None,
            "hipconfig_command_present": shutil.which("hipconfig") is not None,
            "nvcc_command_present": shutil.which("nvcc") is not None,
            "metal_available": None,
            "note": "GPU memory values are MiB; power W, temperature C, utilization percent. A failed query or empty GPU list does not establish GPU absence. Compare sandbox and outside-sandbox execution before choosing CPU-only inference.",
        },
        "disk": {"total_bytes": disk.total, "free_bytes": disk.free,
                 "note": "Filesystem containing the requested target; target path omitted."},
        "python": {"version": platform.python_version(),
                   "packages": {p: version(p) for p in (
                       "torch", "transformers", "accelerate", "vllm", "llama-cpp-python",
                       "huggingface-hub", "google-genai", "safetensors")}},
        "engine_commands_present": {p: shutil.which(p) is not None for p in (
            "ollama", "llama-cli", "llama-server", "llama-bench", "vllm", "lms")},
        "constraints": {
            "cpu_pressure": read("/proc/pressure/cpu"),
            "memory_pressure": read("/proc/pressure/memory"),
            "cpu_power_and_thermals": "not measured; guest access may not expose host values",
            "other_workload_identities": "deliberately not collected",
        },
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--disk-path", default=".")
    parser.add_argument("--output", type=Path)
    parser.add_argument("--execution-scope", choices=['unspecified', 'sandbox', 'outside-sandbox'],
                        default='unspecified', help='Explicit scope label; no automatic privilege inference.')
    args = parser.parse_args()
    payload = json.dumps(inventory(args.disk_path, args.execution_scope), indent=2, ensure_ascii=False) + "\n"
    if args.output:
        # Exclusive creation avoids silently replacing a prior host observation.
        with args.output.open("x", encoding="utf-8") as destination:
            destination.write(payload)
    else:
        print(payload, end="")


if __name__ == "__main__":
    main()
