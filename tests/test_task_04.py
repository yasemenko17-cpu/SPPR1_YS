import os

import pytest
from conftest import load
from cases_task_04 import CASES

run_status = load(4).run_status


@pytest.mark.parametrize("case", CASES, ids=[f"v{(4 - 1) * 3 + c['v']:02d}-{i}" for i, c in enumerate(CASES)])
def test_run_status(tmp_path, case):
    for name, mode, content in case.get("files", []):
        path = tmp_path / name
        path.write_text(content, encoding="utf-8")
        path.chmod(mode)
    argv = [part.format(tmp=tmp_path) for part in case["argv"]]
    assert run_status(argv) == case["expected"]
    with pytest.raises(ChildProcessError):
        os.waitpid(-1, os.WNOHANG)  # дитину дочекано
