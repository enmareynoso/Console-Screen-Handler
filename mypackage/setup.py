# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

try:
    long_description = open("README.rst").read()
except IOError:
    long_description = ""

setup(
    name="add-package",
    version="0.1.0",
    description="Pip package by Enmanuel Reynoso",
    license="MIT",
    author="Enmanuel Reynoso",
    packages=['add-package'],
    install_requires=[],
    long_description=long_description,
    classifiers=[
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.9",
        "License :: OSI Approved :: MIT License"
        "Operating System :: OS Independent"
    ]
)
