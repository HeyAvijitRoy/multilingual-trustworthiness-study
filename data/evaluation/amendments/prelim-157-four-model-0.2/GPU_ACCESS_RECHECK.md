# GPU access correction — 2026-10-23

**A usable NVIDIA GPU is available.** The earlier statement that this host had
no usable GPU resulted from checking device access only inside the sandbox.
That conclusion is retracted. This corrects deployment evidence; it does not
change frozen prompts, annotations, study definitions or model selection.

## Observed hardware and access

Outside-sandbox `nvidia-smi` succeeded:

| Field | Observation |
| --- | --- |
| GPU | NVIDIA A100-SXM4-40GB |
| Total VRAM | 40,960 MiB (40 GiB) |
| Free VRAM | 40,018 MiB (about 39.08 GiB), at the recorded observation |
| Driver | 580.178.04 |
| Utilization | 0%, at the recorded observation |

The new inventories were collected at approximately 19:55 UTC / 3:55 p.m.
America/New_York on 2026-10-23. Free VRAM/utilization are snapshots, not reserved
capacity. Evidence: `HARDWARE_GPU_RECHECK_HOST.json` and
`HARDWARE_GPU_RECHECK_SANDBOX.json`. Earlier inventories remain unchanged as
historical observations; their failed queries describe sandbox visibility.

Inside the sandbox, `nvidia-smi` exits 9 and NVIDIA character-device nodes are
hidden, while PCI identifies the A100 and the NVIDIA driver module is visible.
Outside the sandbox, `/dev/nvidia0`, `/dev/nvidiactl` and the UVM device nodes
are accessible and the same query exits 0. A driver communication failure in the
sandbox therefore does not establish hardware absence or a broken host driver.

## CUDA verification

`CUDA_DRIVER_RECHECK_HOST.json` records a real CUDA driver check outside the
sandbox, using `scripts/check_cuda_driver.py`:

- CUDA initialization succeeded; one device was found and identified as the A100.
- Primary context creation and device-memory querying succeeded.
- Allocation and release of 1 MiB both succeeded; the primary context was released.
- CUDA driver API version reported 13000.

This verifies driver/device-memory access. No model, kernel benchmark, frozen
study generation or paid provider request was run during this recheck.

The existing `.local/inference-venv` contains **torch 2.14.1+cpu**. It reports
`torch.version.cuda = None` and `torch.cuda.is_available() = False` because it is
a CPU-only build. Those results must not be used to reject the detected GPU.
A separate CUDA-enabled inference environment and GPU-access execution scope
are needed before model benchmarking.

## Consequences for the study

The four earlier local runs remain valid measurements of their recorded FP32 CPU
configuration. Their throughput and timeout extrapolations do not describe this
A100. They must not be used to justify a CPU-only deployment decision or rule out
larger GPU-resident contenders. Bengali diagnostic quality concerns remain real
observations of those exact checkpoint/settings/probes; GPU presence alone does
not resolve them.

GPU diagnostics, peak VRAM including KV/runtime overhead, full output allowance,
runtime integration and final two-model selection remain pending. No selected
pair or prospective model-panel freeze is fabricated by this correction.

## Reproduction

Execute these in an environment with host GPU access. In this agent environment,
the successful tool calls used `sandbox_permissions="require_escalated"`.
`--execution-scope` only labels the observation; it does not grant access.

```bash
nvidia-smi --query-gpu=name,memory.total,memory.free,driver_version --format=csv,noheader,nounits
.local/inference-venv/bin/python scripts/hardware_inventory.py --execution-scope outside-sandbox
.local/inference-venv/bin/python scripts/check_cuda_driver.py --execution-scope outside-sandbox
```

The CUDA check allocates and frees only 1 MiB. Optional output files use exclusive
creation to preserve earlier observations. Inventory regression tests now cover
PCI-visible/query-inaccessible hardware and a successful host GPU query, as well
as sanitization and distinguishing directories from device nodes.
The complete repository validation passed with 73 tests on Python 3.11.17;
the inventory, CUDA-check and regression scripts also passed compilation.
