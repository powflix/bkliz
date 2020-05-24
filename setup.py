#!/usr/bin/env python

# Encoding: UTF-8
# Line Endings: LF(Unix)
# Programming Language: Python 3
# Syntax Standard: PEP 8

'''
Author: Abhishek Singh
email: a.s.2013.hts@gmail.com
Source: https://github.com/singh2505/bkliz | see README for more details
License: GNU General Public License v3 (GPLv3) | see LICENSE for more details
Contribution: Wanna contribute to bkliz library? | see CONTRIBUTING for more details

Copyright (C) 2020 Abhishek Singh
'''

import setuptools


with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="bkliz",
    version="1.0.6",
    author="Abhishek Singh",
    author_email="a.s.2013.hts@gmail.com",
    description="A Secure and Powerful Open Source Python Library for Encryption/Decryption.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/singh2505/bkliz",
    packages=setuptools.find_packages(),
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Build Tools",
        "Topic :: Software Development :: Libraries",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: Implementation :: CPython",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
    keywords="python-library pypi-package encryption-decryption utf-8 gplv3",
)
