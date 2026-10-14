import pytest
from conftest import load
from cases_task_01 import CASES

trace_summary = load(1).trace_summary


@pytest.mark.parametrize("case", CASES, ids=[f"v{(1 - 1) * 3 + c['v']:02d}-{i}" for i, c in enumerate(CASES)])
def test_trace_summary(case):
    assert trace_summary(case["trace"], case["top"]) == case["expected"]
