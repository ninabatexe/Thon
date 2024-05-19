import os
import subprocess

def install_packages():
    subprocess.check_call([
        'pip', 'install', '-t', 'wheel2.0',
        'numpy', 'pandas', 'scikit-learn',
        'discord', 'pygame', 'turtle',
        'blackbox', 'transformers'
    ])

if __name__ == '__main__':
    install_packages()