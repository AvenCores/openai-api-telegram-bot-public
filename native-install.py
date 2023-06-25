from sys import executable, platform
import subprocess


if platform == "win32":
    subprocess.run([executable, "-m", "pip", "install", "-r", "requirements.txt"])

if platform.startswith("linux"):
    subprocess.run([executable, "-m", "pip", "install", "-r", "requirements.txt"])
