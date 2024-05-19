import os
import subprocess

def install_thon():
    subprocess.check_call([
        'pip', 'install', 'Thon',
    ])

def install_packages():
    subprocess.check_call([
        'python', 'update.py',
    ])
if __name__ == '__main__':
    install_thon()
    install_packages()