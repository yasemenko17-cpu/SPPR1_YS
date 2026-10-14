import os
import time

import pytest
from conftest import load
from cases_task_08 import CASES

spawn_orphans = load(8).spawn_orphans


def read_lines(path):
    try:
        with open(path, encoding="utf-8") as handle:
            return handle.read().splitlines()
    except FileNotFoundError:
        return []


@pytest.mark.parametrize("case", CASES, ids=[f"v{(8 - 1) * 3 + c['v']:02d}-{i}" for i, c in enumerate(CASES)])
def test_spawn_orphans(tmp_path, case):
    path = tmp_path / "orphans.txt"
    old = []
    if case.get("old"):
        path.write_text("старий рядок\n", encoding="utf-8")
        old = ["старий рядок"]
    n, label = case["n"], case["label"]
    started = time.monotonic()
    assert spawn_orphans(str(path), n, label) == 0
    assert time.monotonic() - started < 3, "функція не повинна чекати онуків"
    expected = sorted(old + [f"{label} {k}: усиновлено" for k in range(1, n + 1)])
    deadline = time.monotonic() + 8
    while time.monotonic() < deadline and len(read_lines(path)) < len(expected):
        time.sleep(0.02)
    assert sorted(read_lines(path)) == expected
    with pytest.raises(ChildProcessError):
        os.waitpid(-1, os.WNOHANG)  # дитину дочекано, онуків батько не чекає
