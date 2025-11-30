import sys
import ctypes
import os


def attach_or_create_console():
    attached = ctypes.windll.kernel32.AttachConsole(-1)  # ATTACH_PARENT_PROCESS
    if not attached:
        ctypes.windll.kernel32.AllocConsole()

    # stdin/stdout/stderr
    sys.stdout = open("CONOUT$", "w", encoding="utf-8", buffering=1)
    sys.stderr = open("CONOUT$", "w", encoding="utf-8", buffering=1)
    sys.stdin = open("CONIN$", "r", encoding="utf-8", buffering=1)
