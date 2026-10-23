#!/usr/bin/env python3
"""Check CUDA access without PyTorch/model loads; allocate/free only 1 MiB.

Run separately inside and outside the sandbox. The installed PyTorch build may
be CPU-only, so torch.cuda.is_available() alone does not diagnose host hardware.
Outputs omit hostnames, UUIDs, PCI addresses, process identities and secrets.
"""
import argparse
import ctypes as c
import ctypes.util
from datetime import datetime, timezone
import importlib.metadata
import json
from pathlib import Path


def check(scope='unspecified'):
    result = {'observed_at_utc': datetime.now(timezone.utc).isoformat(),
              'observation_scope': scope, 'allocation_test_bytes': 1024 * 1024}
    try:
        result['installed_torch_version'] = importlib.metadata.version('torch')
    except importlib.metadata.PackageNotFoundError:
        result['installed_torch_version'] = None
    library = ctypes.util.find_library('cuda')
    if library is None:
        return {**result, 'cuda_access_verified': False, 'reason': 'CUDA driver library not found'}
    try:
        lib = c.CDLL(library)
    except OSError:
        return {**result, 'cuda_access_verified': False, 'reason': 'CUDA driver library could not load'}
    signatures = {
        'cuInit': [c.c_uint], 'cuDeviceGetCount': [c.POINTER(c.c_int)],
        'cuDriverGetVersion': [c.POINTER(c.c_int)],
        'cuDeviceGet': [c.POINTER(c.c_int), c.c_int],
        'cuDeviceGetName': [c.c_char_p, c.c_int, c.c_int],
        'cuDevicePrimaryCtxRetain': [c.POINTER(c.c_void_p), c.c_int],
        'cuCtxSetCurrent': [c.c_void_p],
        'cuMemGetInfo_v2': [c.POINTER(c.c_size_t), c.POINTER(c.c_size_t)],
        'cuMemAlloc_v2': [c.POINTER(c.c_uint64), c.c_size_t],
        'cuMemFree_v2': [c.c_uint64], 'cuDevicePrimaryCtxRelease_v2': [c.c_int],
    }
    for name, args in signatures.items():
        getattr(lib, name).argtypes = args
        getattr(lib, name).restype = c.c_int

    def call(name, *args):
        status = getattr(lib, name)(*args)
        result[name + '_status'] = status
        return status == 0

    result['cuda_access_verified'] = False
    version, count, device = c.c_int(), c.c_int(), c.c_int()
    if not call('cuInit', 0):
        return result
    if call('cuDriverGetVersion', c.byref(version)):
        result['cuda_driver_api_version'] = version.value
    if not call('cuDeviceGetCount', c.byref(count)):
        return result
    result['cuda_device_count'] = count.value
    if not count.value or not call('cuDeviceGet', c.byref(device), 0):
        return result
    name = c.create_string_buffer(256)
    if call('cuDeviceGetName', name, len(name), device):
        result['cuda_device_name'] = name.value.decode()
    context = c.c_void_p()
    if not call('cuDevicePrimaryCtxRetain', c.byref(context), device):
        return result
    try:
        if not call('cuCtxSetCurrent', context):
            return result
        free, total = c.c_size_t(), c.c_size_t()
        if call('cuMemGetInfo_v2', c.byref(free), c.byref(total)):
            result.update(free_bytes=free.value, total_bytes=total.value)
        pointer = c.c_uint64()
        if call('cuMemAlloc_v2', c.byref(pointer), result['allocation_test_bytes']):
            result['cuda_access_verified'] = call('cuMemFree_v2', pointer)
    finally:
        call('cuCtxSetCurrent', None)
        call('cuDevicePrimaryCtxRelease_v2', device)
    return result


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--execution-scope', choices=['unspecified', 'sandbox', 'outside-sandbox'], default='unspecified')
    parser.add_argument('--output', type=Path)
    args = parser.parse_args()
    result = check(args.execution_scope)
    encoded = json.dumps(result, indent=2) + '\n'
    if args.output:
        with args.output.open('x', encoding='utf-8') as destination:
            destination.write(encoded)
    else:
        print(encoded, end='')
    return 0 if result['cuda_access_verified'] else 3


if __name__ == '__main__':
    raise SystemExit(main())
