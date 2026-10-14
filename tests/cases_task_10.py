"""Відкриті приклади (вони є на картках варіантів). Повний набір - у викладача."""

CASES = [{'v': 1, 'public': True, 'argv': ['env', 'true'], 'programs': ['env', 'true'], 'code': 0},
 {'v': 2,
  'public': True,
  'argv': ['sh', '-c', '/bin/true; /bin/true; exit 4'],
  'programs': ['sh', 'true', 'true'],
  'code': 4},
 {'v': 3, 'public': True, 'argv': ['no_such_program_zz'], 'programs': [], 'code': 1}]
