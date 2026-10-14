import pytest
from variants.variant_08 import spawn_orphans

@pytest.mark.parametrize("n, label", [
    (0, "тест-нуль"),
    (3, "тест-сирота"),
])
def test_my_edge_cases(tmp_path, n, label):
    path = tmp_path / "my_test.txt"
    result = spawn_orphans(str(path), n, label)
    assert result == 0
    if n > 0:
        assert path.exists()
        content = path.read_text(encoding="utf-8")
        assert f"{label} 1: усиновлено" in content