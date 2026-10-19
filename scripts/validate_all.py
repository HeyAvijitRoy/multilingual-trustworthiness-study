"""Run the complete local pre-evaluation validation suite."""
from pathlib import Path
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]

COMMANDS = [
    [sys.executable, 'scripts/validate_prompt_corpus.py'],
    [sys.executable, 'scripts/freeze_prompt_corpus.py', '--check'],
    [sys.executable, 'scripts/validate_pilot_annotations.py'],
    [sys.executable, '-m', 'unittest', 'discover', '-s', 'scripts', '-p', 'test_*.py'],
    [sys.executable, 'scripts/prepare_scaling_queue.py', '--check'],
    [sys.executable, 'scripts/prepare_expansion_batches.py', '--check'],
    [sys.executable, 'scripts/calibration.py', 'check'],
    ['git', 'diff', '--check'],
]


def main():
    for command in COMMANDS:
        print('+', ' '.join(command), flush=True)
        subprocess.run(command, cwd=ROOT, check=True)
    print('FULL LOCAL VALIDATION PASSED')


if __name__ == '__main__':
    try:
        main()
    except subprocess.CalledProcessError as exc:
        raise SystemExit(f'FULL LOCAL VALIDATION FAILED (exit {exc.returncode})')
