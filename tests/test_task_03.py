import os

import pytest
from conftest import load
from cases_task_03 import CASES

count_nodes = load(3).count_nodes


@pytest.mark.parametrize("case", CASES, ids=[f"v{(3 - 1) * 3 + c['v']:02d}-{i}" for i, c in enumerate(CASES)])
def test_count_nodes(tmp_path, monkeypatch, case):
    log = tmp_path / "forks.log"
    real_fork = os.fork

    def counting_fork():
        with open(log, "ab") as handle:
            handle.write(b"x")  # один запис - один виклик fork (також у дітях)
        return real_fork()

    monkeypatch.setattr(os, "fork", counting_fork)
    assert count_nodes(case["shape"]) == case["size"]
    forks = log.stat().st_size if log.exists() else 0
    assert forks == case["size"] - 1, "кожен вузол, крім кореня, має бути окремим процесом (os.fork)"
    with pytest.raises(ChildProcessError):
        os.waitpid(-1, os.WNOHANG)  # усіх дітей дочекано, зомбі немає
