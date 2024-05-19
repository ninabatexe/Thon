import os
import subprocess

def uninstall_thon():
    subprocess.check_call([
        'pip', 'uninstall', '-y', 'Thon',
    ])

def remove_wheel2_0():
    if os.path.exists('wheel2.0'):
        subprocess.check_call(['rm', '-rf', 'wheel2.0'])

if __name__ == '__main__':
    uninstall_thon()
    remove_wheel2_0()