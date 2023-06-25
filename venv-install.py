from sys import platform
import subprocess
import os


activate_script_windows = os.path.join("venv", "Scripts", "activate")
activate_script_linux = os.path.join("venv", "bin", "activate")

if not os.path.isdir("venv"):
    subprocess.run(["python", "-m", "venv", "venv"])

if platform == "win32":
    subprocess.run([f"cmd /c {activate_script_windows} && pip install -r requirements.txt"], shell=True)

if platform.startswith("linux"):
    subprocess.run([f"source {activate_script_linux} && pip3 install -r requirements.txt"], shell=True)
