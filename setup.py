"""Script that installs 'allo' package.

To install one should run 'pip3 install .' command. 
Afterwards, you will be able to run the package
using 'allo' command.
"""

from setuptools import setup, find_packages

setup(
    name='allo',
    version='1.0',
    packages=find_packages(),
    include_package_data = True,
    install_requires=('Scrapy>=2.0.0',),
    entry_points={
        'console_scripts': (
            'allo=allo.main:run',
        )
    }
)
