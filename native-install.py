from sys import platform
import subprocess


if platform == "win32":
    subprocess.run(["pip", "install", "-r", "requirements.txt"], shell=True)

if platform == "linux" or platform == "linux2" or platform == "unix":
    subprocess.run(["pip3", "install", "-r", "requirements.txt"], shell=True)