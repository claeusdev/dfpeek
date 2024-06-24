import subprocess


def display():
    return subprocess.Popen(["dfexplore"], stdout=subprocess.PIPE)
