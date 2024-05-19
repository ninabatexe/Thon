import os
import subprocess

packages = {
    'Thon1': 'version1',
    'Thon 2': 'version2',
}

def install_packages():
    for package, version in packages.items():
        subprocess.check_call([
            'pip', 'install', package, '==', version
        ])

def check_wheel_installation():
    if not os.path.exists('wheel2.0'):
        subprocess.check_call(['pip', 'install', '-t', 'wheel2.0'])

if __name__ == '__main__':
    install_packages()
    check_wheel_installation()