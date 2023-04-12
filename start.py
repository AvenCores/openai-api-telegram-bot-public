from sys import platform
import subprocess
import os

activate_script_windows = os.path.join("venv", "Scripts", "activate")
activate_script_linux = os.path.join("venv", "bin", "activate")

if platform == "win32":
    subprocess.run([f"call {activate_script_windows} && python main.py %*"], shell=True)

if platform == "linux" or platform == "linux2" or platform == "unix":
    subprocess.run([f"source {activate_script_linux} && python3 main.py"], shell=True)