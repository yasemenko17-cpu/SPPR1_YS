import os
import time

import pytest
from conftest import load
from cases_task_07 import CASES

run_parallel = load(7).run_parallel


@pytest.mark.parametrize("case", CASES, ids=[f"v{(7 - 1) * 3 + c['v']:02d}-{i}" for i, c in enumerate(CASES)])
def test_run_parallel(case):
    started = time.monotonic()
    codes, first = run_parallel(case["commands"])
    elapsed = time.monotonic() - started
    assert (codes, first) == (case["codes"], case["first"])
    if "max_time" in case:
        assert elapsed < case["max_time"], f"команди мали працювати одночасно (пройшло {elapsed:.2f} с)"
    with pytest.raises(ChildProcessError):
        os.waitpid(-1, os.WNOHANG)  # усіх дітей дочекано
