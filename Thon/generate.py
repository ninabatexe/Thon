import os
import shutil
import subprocess

def generate_thon():
    
    os.makedirs('ThonPC', exist_ok=True)
    
    shutil.copy('Thon/main.py', 'ThonPC/')
    shutil.copy('Thon/__init__.py', 'ThonPC/')

    subprocess.run(['python', 'Thon/install.py'])
    print('Thon generated successfully.')

if __name__ == '__main__':
    generate_thon()