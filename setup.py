from setuptools import setup, find_packages

setup(
    name='SecretFinder',
    version='1.0.0',
    description='Tool for discovering API keys, access tokens, and sensitive data in JS files.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='m4ll0k',
    author_email='m4ll0k2@gmail.com',
    url='https://github.com/m4ll0k/SecretFinder',
    packages=find_packages(),
    install_requires=[
        'requests',              # Required for HTTP requests
        'requests-file',         # Support for reading local files with file://
        'lxml',                  # Required for parsing HTML
        'jsbeautifier',          # Beautifier for JS files
    ],
    entry_points={
        'console_scripts': [
            'secretfinder = SecretFinder:main',
        ],
    },
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',  # Assumes Python 3.6 or higher
    include_package_data=True,
)
