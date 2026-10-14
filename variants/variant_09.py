"""Практична робота SP-P01. Задача 09: Шукає виконуваний файл за правилами PATH, як це робить exec з p.

Реалізуйте функцію за карткою свого варіанта. Введення й виведення - лише в блоці __main__.
"""

VARIANT = 0  # впишіть номер свого варіанта (1-30)


def which(program: str, path: str, cwd: str) -> str | None:
    """Шукає виконуваний файл за правилами PATH, як це робить exec з p."""
    raise NotImplementedError  # TODO: реалізуйте за карткою


if __name__ == "__main__":
    print("Запустіть тести: pytest --variant", VARIANT)
