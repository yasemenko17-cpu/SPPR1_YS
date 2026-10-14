"""Відкриті приклади (вони є на картках варіантів). Повний набір - у викладача."""

CASES = [{'v': 1,
  'public': True,
  'files': ['a.txt', 'd/b.txt'],
  'dirs': ['d', 'empty'],
  'ops': [('stat', 'a.txt', 'OK'), ('stat', 'missing.txt', 'ENOENT')]},
 {'v': 2,
  'public': True,
  'files': ['a.txt'],
  'dirs': ['d'],
  'ops': [('open_w', 'a.txt', 'OK'), ('open_w', 'nope.txt', 'ENOENT')]},
 {'v': 3,
  'public': True,
  'files': ['f.txt', 'full/x.txt'],
  'dirs': ['empty', 'full'],
  'ops': [('mkdir', 'new', 'OK'), ('mkdir', 'empty', 'EEXIST')]}]
