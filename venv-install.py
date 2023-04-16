from sys import platform
import subprocess
import os

activate_script_windows = os.path.join("venv", "Scripts", "activate")
activate_script_linux = os.path.join("venv", "bin", "activate")

if platform == "win32":
    subprocess.run(["python", "-m", "venv", "venv"])
    subprocess.run([f"call", "{activate_script_windows}", "&&", "pip", "install", "-r", "requirements.txt"], shell=True)

if platform == "linux" or platform == "linux2" or platform == "unix":
    subprocess.run(["python3", "-m", "venv", "venv"])
    subprocess.run([f"source," f"{activate_script_linux}", "&&", "pip3", "install", "-r", "requirements.txt"], shell=True)