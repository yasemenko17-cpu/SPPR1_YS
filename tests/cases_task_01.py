"""Відкриті приклади (вони є на картках варіантів). Повний набір - у викладача."""

CASES = [{'v': 1,
  'public': True,
  'trace': 'execve("/usr/bin/ls", ["ls"], 0x7ffd /* 30 vars */) = 0\n'
           'brk(NULL)                               = 0x55d0c8a2b000\n'
           'openat(AT_FDCWD, "/etc/ld.so.cache", O_RDONLY|O_CLOEXEC) = 3\n'
           'openat(AT_FDCWD, "/lib/libc.so.6", O_RDONLY|O_CLOEXEC) = 3\n'
           'read(3, "\\177ELF\\2\\1\\1\\3\\0\\0\\0\\0\\0\\0\\0\\0\\3\\0>\\0\\1\\0\\0\\0", 832) = 832\n'
           'openat(AT_FDCWD, "/nonexistent", O_RDONLY) = -1 ENOENT (No such file or directory)\n'
           'write(1, "a.txt\\n", 6)                  = 6\n'
           'write(1, "b.txt\\n", 6)                  = 6\n'
           'close(3)                                = 0\n'
           '+++ exited with 0 +++\n',
  'top': 3,
  'expected': 'Усього викликів: 9\nНевдалих: 1\nНайчастіші:\nopenat: 3\nwrite: 2\nbrk: 1'},
 {'v': 2,
  'public': True,
  'trace': '[pid 3001] execve("/usr/bin/sh", ["sh", "-c", "ls"], 0x7ffd /* 10 vars */) = 0\n'
           '[pid 3001] clone(child_stack=NULL, flags=CLONE_CHILD_CLEARTID|SIGCHLD) = 3002\n'
           '[pid 3002] execve("/usr/bin/ls", ["ls"], 0x7ffd /* 10 vars */) = 0\n'
           '[pid 3002] openat(AT_FDCWD, "/nope", O_RDONLY) = -1 ENOENT (No such file or directory)\n'
           '[pid 3001] wait4(-1,  <unfinished ...>\n'
           '[pid 3002] +++ exited with 0 +++\n'
           '[pid 3001] <... wait4 resumed>[{WIFEXITED(s) && WEXITSTATUS(s) == 0}], 0, NULL) = 3002\n'
           '[pid 3001] --- SIGCHLD {si_signo=SIGCHLD} ---\n'
           '[pid 3001] exit_group(0) = ?\n'
           '[pid 3001] +++ exited with 0 +++\n',
  'top': 2,
  'expected': 'Усього викликів: 6\nНевдалих: 1\nНайчастіші:\nexecve: 2\nclone: 1'},
 {'v': 3,
  'public': True,
  'trace': '12:00:01.123456 openat(AT_FDCWD, "/etc/hosts", O_RDONLY) = 3 <0.000021>\n'
           '12:00:01.123600 fstat(3, {st_mode=S_IFREG|0644, st_size=221, ...}) = 0 <0.000008>\n'
           '12:00:01.123700 read(3, "127.0.0.1 localhost\\n", 4096) = 221 <0.000012>\n'
           '12:00:01.123800 read(3, "", 4096)       = 0 <0.000006>\n'
           '12:00:01.123900 close(3)                = 0 <0.000009>\n'
           '12:00:01.124000 openat(AT_FDCWD, "/etc/missing", O_RDONLY) = -1 ENOENT (No such file or '
           'directory) <0.000010>\n'
           '12:00:01.124100 write(1, "done\\n", 5)   = 5 <0.000015>\n',
  'top': 2,
  'expected': 'Усього викликів: 7\nНевдалих: 1\nНайчастіші:\nopenat: 2\nread: 2'}]
