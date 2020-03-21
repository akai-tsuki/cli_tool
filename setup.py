# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

with open('requirements.txt') as requirements_file:
    install_requirements = requirements_file.read().splitlines()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='cli_tool',
    version='0.1.0',
    description='Study Cli Tool',
    url='https://github.com/akai-tsuki/cli_tool',
    license=license,
    packages=find_packages(exclude=('tests', 'docs')),
    install_requires=install_requirements,
    entry_points={
        "console_scripts": [
            "sample=cli_tool.core:main",
        ]
    },
    classifiers=[
        'Programming Language :: Python :: 2.7',
    ]

)
