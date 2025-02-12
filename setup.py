from setuptools import setup, find_packages

setup(
    name="secretfinder", 
    version="1.0.0",  
    packages=find_packages(),  
    install_requires=open('requirements.txt').read().splitlines(), 
    entry_points={  
        'console_scripts': [
            'secretfinder = secretfinder.main:main',  
        ],
    },
)
