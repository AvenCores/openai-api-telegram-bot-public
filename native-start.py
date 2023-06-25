from sys import platform, executable, argv
import subprocess


if platform == "win32":
    subprocess.run([executable, "main.py"] + argv[1:])

if platform.startswith("linux"):
    subprocess.run([executable, "main.py"] + argv[1:])