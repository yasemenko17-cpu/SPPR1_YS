import os

import pytest
from conftest import load
from cases_task_05 import CASES

child_env_lines = load(5).child_env_lines


@pytest.mark.parametrize("case", CASES, ids=[f"v{(5 - 1) * 3 + c['v']:02d}-{i}" for i, c in enumerate(CASES)])
def test_child_env_lines(monkeypatch, case):
    for name in [n for n in os.environ if n.startswith(("SPT_", "NOPE_", "OTHER"))]:
        monkeypatch.delenv(name)
    for name, value in case["parent"].items():
        monkeypatch.setenv(name, value)
    snapshot = dict(os.environ)
    result = child_env_lines(case["prefix"], case["set"], case["unset"])
    assert result == case["expected"]
    assert dict(os.environ) == snapshot, "оточення батьківського процесу змінювати не можна"
