import pytest
from conftest import load
from cases_task_10 import CASES

traced_programs = load(10).traced_programs


@pytest.mark.parametrize("case", CASES, ids=[f"v{(10 - 1) * 3 + c['v']:02d}-{i}" for i, c in enumerate(CASES)])
def test_traced_programs(case):
    programs, code = traced_programs(case["argv"])
    assert (programs, code) == (case["programs"], case["code"])
