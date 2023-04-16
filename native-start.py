from sys import platform
import subprocess


if platform == "win32":
    subprocess.run(["python", "main.py", "%*"], shell=True)

if platform == "linux" or platform == "linux2" or platform == "unix":
    subprocess.run(["python3", "main.py"], shell=True)