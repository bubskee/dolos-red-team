"""Verify saved publication evidence; never starts model inference."""
import argparse
from pathlib import Path
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--full', action='store_true',
                        help='also run audit tests and NumPy/Torch-dependent integrity checks')
    args = parser.parse_args()
    commands = [
        ['audit/replay.py', '--verify'],
        ['report/review_checks.py'],
    ]
    if args.full:
        commands += [
            ['-m', 'unittest', 'discover', '-s', 'audit/v1', '-p', 'test*.py'],
            ['-m', 'unittest', 'discover', '-s', 'audit/v2', '-p', 'test*.py'],
            ['audit/v1/verify_run.py'],
            ['audit/v2/verify_run.py', '--completed-only'],
            ['audit/v2/verify_priority.py'],
        ]
    for command in commands:
        print('Running:', sys.executable, *command, flush=True)
        subprocess.run([sys.executable, *command], cwd=ROOT, check=True)
    print('Saved-evidence checks passed. No model inference performed.')


if __name__ == '__main__':
    main()
