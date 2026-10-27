"""Test helpers: import the numbered step scripts and redirect results to a temporary folder."""
import importlib.util
import shutil
import sys
import tempfile
from pathlib import Path

SCRIPTS = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(SCRIPTS))

import common  # noqa: E402


def step(name):
    """Import scripts/<name>.py (e.g. '04_score') as a module."""
    spec = importlib.util.spec_from_file_location('step_' + name, SCRIPTS / f'{name}.py')
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


class TempResults:
    """Copy (part of) results/ into a temp folder and point the given modules at it."""

    def __init__(self, *modules, copy=('responses', 'scores', 'validation')):
        self.modules, self.copy = modules, copy

    def __enter__(self):
        self.dir = Path(tempfile.mkdtemp())
        for sub in self.copy:
            if (common.RESULTS / sub).exists():
                shutil.copytree(common.RESULTS / sub, self.dir / sub, ignore=shutil.ignore_patterns('*.result.json'))
        self.saved = [(m, m.RESULTS) for m in self.modules]
        for m in self.modules:
            m.RESULTS = self.dir
        return self.dir

    def __exit__(self, *exc):
        for m, value in self.saved:
            m.RESULTS = value
        shutil.rmtree(self.dir)


def rating(item_id, score, reason=None):
    if reason is None:
        reason = ('pass' if score == 1 else 'fail') if item_id.startswith('CHECK') else \
            {1: 'met', 0.5: 'partial', 0: 'omitted'}[score]
    return {'item_id': item_id, 'score': score, 'reason': reason, 'evidence': '', 'notes': ''}


def perfect_ratings(rec):
    return [rating(r['id'], 1) for r in rec['rius']] + [rating(c['id'], 1) for c in rec.get('task_checks', [])]
