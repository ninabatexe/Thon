from setuptools import setup, find_packages

setup(
    name='ThonPC',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        'pygame',
        'discord.py',
        'turtle',
        'pandas',
        'numpy',
        'sklearn'
        
    ],
    package_dir={'': 'ThonPC'},
    entry_points={
        'console_scripts': [
            'thonpc = ThonPC.main:main',
        ],
    },
)