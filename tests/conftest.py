"""Допоміжний завантажувач: підключає файл варіанта з теки variants/."""
import importlib.util
import os
from pathlib import Path

ROOT = Path(__file__).resolve().parent


def pytest_addoption(parser):
    parser.addoption("--variant", type=int, default=0,
                     help="номер варіанта 1-30: запускати лише його тести")


def pytest_collection_modifyitems(config, items):
    number = config.getoption("--variant")
    if not number:
        return
    marker = f"[v{number:02d}-"
    chosen = [item for item in items if marker in item.nodeid]
    config.hook.pytest_deselected(items=[item for item in items if item not in chosen])
    items[:] = chosen


def load(number):
    """Повертає модуль варіанта з номером number."""
    base = Path(os.environ.get("VARIANT_DIR", ROOT.parent / "variants"))
    for prefix in ("variant", "lab", "task"):
        path = base / f"{prefix}_{number:02d}.py"
        if path.exists():
            spec = importlib.util.spec_from_file_location(f"{prefix}_{number:02d}", path)
            module = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(module)
            return module
    raise FileNotFoundError(f"Не знайдено файл варіанта {number:02d} у {base}")
