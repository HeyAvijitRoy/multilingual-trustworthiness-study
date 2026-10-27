import contextlib
import importlib.util
import io
import json
import os
import unittest

from helpers import TempResults, common

NOTEBOOK = common.ROOT / 'notebooks/analysis.ipynb'


class NotebookTest(unittest.TestCase):
    def test_code_cells_run_in_order(self):
        """Execute every code cell top to bottom, against a temporary copy of results/."""
        cells = [''.join(c['source']) for c in json.loads(NOTEBOOK.read_text())['cells'] if c['cell_type'] == 'code']
        if importlib.util.find_spec('IPython') is None:
            cells[0] = cells[0].replace('from IPython.display import Image, Markdown, display',
                                        'display = Markdown = Image = lambda *a, **k: None')
        namespace, cwd = {}, os.getcwd()
        os.chdir(NOTEBOOK.parent)
        try:
            exec(cells[0], namespace)
            modules = [namespace[n] for n in ('judge', 'status', 'analysis')]
            with TempResults(*modules) as tmp, contextlib.redirect_stdout(io.StringIO()):
                namespace['RESULTS'] = tmp
                for cell in cells[1:]:
                    exec(cell, namespace)
                self.assertTrue((tmp / 'analysis/critical_omission_effects.png').exists())
        finally:
            os.chdir(cwd)


if __name__ == '__main__':
    unittest.main()
