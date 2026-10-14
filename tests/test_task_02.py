import os

import pytest
from conftest import load
from cases_task_02 import CASES

probe_paths = load(2).probe_paths


def build(base, case):
    for name in case["dirs"]:
        os.makedirs(base / name, exist_ok=True)
    for name in case["files"]:
        os.makedirs((base / name).parent, exist_ok=True)
        (base / name).write_text("x", encoding="utf-8")


@pytest.mark.parametrize("case", CASES, ids=[f"v{(2 - 1) * 3 + c['v']:02d}-{i}" for i, c in enumerate(CASES)])
def test_probe_paths(tmp_path, case):
    build(tmp_path, case)
    ops = [(op, str(tmp_path / rel)) for op, rel, _ in case["ops"]]
    expected = [f"{op} {tmp_path / rel}: {code}" for op, rel, code in case["ops"]]
    assert probe_paths(ops) == expected
