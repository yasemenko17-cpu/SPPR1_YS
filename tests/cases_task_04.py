"""Відкриті приклади (вони є на картках варіантів). Повний набір - у викладача."""

CASES = [{'v': 1, 'public': True, 'argv': ['sh', '-c', 'exit 3'], 'expected': 'Код повернення: 3'},
 {'v': 2,
  'public': True,
  'argv': ['sh', '-c', 'kill -s TERM $$'],
  'expected': 'Завершено сигналом 15 (SIGTERM)'},
 {'v': 3, 'public': True, 'argv': ['no_such_program_zz'], 'expected': 'Програму не знайдено'}]
