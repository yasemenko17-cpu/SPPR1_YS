import os
import signal
import subprocess
import time

import pytest
from conftest import load
from cases_task_06 import CASES

proc_status = load(6).proc_status


def field(pid, key):
    try:
        with open(f"/proc/{pid}/status", encoding="utf-8") as handle:
            for line in handle:
                if line.startswith(key + ":"):
                    return line.split(":", 1)[1].strip()
    except OSError:
        return None
    return None


def wait_for(pid, key, test, timeout=5.0):
    end = time.monotonic() + timeout
    while time.monotonic() < end:
        value = field(pid, key)
        if value is not None and test(value):
            return
        time.sleep(0.01)
    raise AssertionError(f"процес {pid} не досяг очікуваного стану ({key})")


def comm_of_self():
    with open("/proc/self/comm", encoding="utf-8") as handle:
        return handle.read().strip()


@pytest.mark.parametrize("case", CASES, ids=[f"v{(6 - 1) * 3 + c['v']:02d}-{i}" for i, c in enumerate(CASES)])
def test_proc_status(tmp_path, case):
    kind = case["kind"]
    me = os.getpid()
    if kind in ("sleep", "stopped", "sleep_named"):
        program = "sleep"
        if kind == "sleep_named":
            program = str(tmp_path / case["name"])
            with open(program, "w", encoding="utf-8") as handle:
                handle.write("#!/bin/sh\nsleep 30\n")
            os.chmod(program, 0o755)
        child = subprocess.Popen([program, "30"], start_new_session=True)
        try:
            name = case.get("name", "sleep")[:15]
            wait_for(child.pid, "Name", lambda v: v == name)
            wait_for(child.pid, "State", lambda v: v.startswith("S"))
            letter, label = "S", "сплить"
            if kind == "stopped":
                os.kill(child.pid, signal.SIGSTOP)
                wait_for(child.pid, "State", lambda v: v.startswith("T"))
                letter, label = "T", "зупинений"
            expected = f"Ім'я: {name}\nСтан: {letter} ({label})\nPPID: {me}\nПотоків: 1"
            assert proc_status(child.pid) == expected
        finally:
            os.killpg(child.pid, signal.SIGKILL)
            child.wait()
    elif kind.startswith("zombie"):
        pid = os.fork()
        if pid == 0:
            if kind == "zombie_killed":
                os.kill(os.getpid(), signal.SIGKILL)
            os._exit(case.get("code", 0))
        try:
            wait_for(pid, "State", lambda v: v.startswith("Z"))
            if kind == "zombie_reaped":
                os.waitpid(pid, 0)
                assert proc_status(pid) == "Процес не знайдено"
            else:
                expected = f"Ім'я: {comm_of_self()}\nСтан: Z (зомбі)\nPPID: {me}\nПотоків: 1"
                assert proc_status(pid) == expected
        finally:
            try:
                os.waitpid(pid, 0)
            except ChildProcessError:
                pass
    elif kind == "invalid":
        assert proc_status(case["pid"]) == "Некоректний PID"
    elif kind == "missing":
        child = subprocess.Popen(["true"])
        child.wait()
        assert proc_status(child.pid) == "Процес не знайдено"
    elif kind == "huge":
        assert proc_status(2**31 - 1) == "Процес не знайдено"
    elif kind == "self":
        expected = (f"Ім'я: {comm_of_self()}\nСтан: R (виконується)\nPPID: {os.getppid()}\n"
                    f"Потоків: {len(os.listdir('/proc/self/task'))}")
        assert proc_status(me) == expected
    else:
        raise AssertionError(kind)
