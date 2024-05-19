import os
import subprocess

def build_thon():
    subprocess.check_call([
        'python', 'setup.py', 'bdist_wheel',
    ])

if __name__ == '__main__':
    build_thon()