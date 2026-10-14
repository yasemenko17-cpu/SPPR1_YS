"""Практична робота SP-P01. Задача 06: Розбирає /proc/<pid>/status і описує стан процесу.

Реалізуйте функцію за карткою свого варіанта. Введення й виведення - лише в блоці __main__.
"""

VARIANT = 0  # впишіть номер свого варіанта (1-30)


def proc_status(pid: int) -> str:
    """Розбирає /proc/<pid>/status і описує стан процесу."""
    raise NotImplementedError  # TODO: реалізуйте за карткою


if __name__ == "__main__":
    print("Запустіть тести: pytest --variant", VARIANT)
