#!/usr/bin/env python
from setuptools import setup, find_packages

setup(
    name='SecretFinder',
    packages=find_packages(),
    version='1.0',
    long_description=open('README.md').read(),
    url='https://github.com/angelopassaro/SecretFinder',
    py_modules=['secretfinder'],
    install_requires=['requests','requests-file','lxml','jsbeautifier'],
)
