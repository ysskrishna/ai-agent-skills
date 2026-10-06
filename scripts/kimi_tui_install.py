#!/usr/bin/env python3
"""Install a local plugin into Kimi Code by driving its TUI through a pseudo-terminal.

Kimi has no `kimi plugins` subcommand, only the `/plugins install` slash command.
Usage: kimi_tui_install.py HOME PLUGIN_DIR
Exit code 0 when Kimi prints "Installed <name>", 1 otherwise.
"""
import os
import pty
import re
import select
import sys
import time

HOME, PLUGIN = sys.argv[1], sys.argv[2]
env = dict(os.environ, HOME=HOME, KIMI_CODE_HOME=f"{HOME}/.kimi-code", TERM="xterm-256color")

pid, fd = pty.fork()
if pid == 0:
    os.chdir(HOME)
    os.execvpe("kimi", ["kimi"], env)


def pump(seconds):
    out, end = b"", time.time() + seconds
    while time.time() < end:
        ready, _, _ = select.select([fd], [], [], 0.3)
        if ready:
            try:
                out += os.read(fd, 65536)
            except OSError:
                break
    return out


def send(text):
    for ch in text:
        os.write(fd, ch.encode())
        time.sleep(0.03)


buf = pump(8)
os.write(fd, b"\r")  # "Trust this folder?" is the default choice
buf += pump(4)
send(f"/plugins install {PLUGIN}")
buf += pump(1.5)
os.write(fd, b"\r")
buf += pump(5)
os.write(fd, b"\x1b[B")  # move to "Trust and install"
buf += pump(1.5)
os.write(fd, b"\r")
buf += pump(15)
os.kill(pid, 9)

text = re.sub(rb"\x1b\[[0-9;?]*[ -/]*[@-~]|\x1b\][^\x07]*\x07", b"", buf).decode("utf8", "ignore")
print(text[-1500:])
ok = re.search(r"Installed \S+ \S+ from", text) is not None
sys.exit(0 if ok else 1)
