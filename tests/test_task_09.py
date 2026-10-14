import os

import pytest
from conftest import load
from cases_task_09 import CASES

which = load(9).which


@pytest.mark.parametrize("case", CASES, ids=[f"v{(9 - 1) * 3 + c['v']:02d}-{i}" for i, c in enumerate(CASES)])
def test_which(tmp_path, monkeypatch, case):
    root = tmp_path / "root"
    elsewhere = tmp_path / "elsewhere"
    root.mkdir()
    elsewhere.mkdir()
    for name in case["dirs"]:
        os.makedirs(root / name, exist_ok=True)
    for name, mode in case["files"]:
        os.makedirs((root / name).parent, exist_ok=True)
        (root / name).write_text("#!/bin/sh\nexit 0\n", encoding="utf-8")
        (root / name).chmod(mode)
    for name, target in case.get("links", []):
        os.makedirs((root / name).parent, exist_ok=True)
        os.symlink(target, root / name)
    monkeypatch.chdir(elsewhere)  # поточний каталог процесу не збігається з cwd із аргументів
    result = which(case["program"].format(tmp=root), case["path"].format(tmp=root), str(root))
    expected = case["expected"]
    assert result == (expected.format(tmp=root) if expected else None)
