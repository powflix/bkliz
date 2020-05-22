# Encoding: UTF-8
# Line Endings: LF(Unix)
# Programming Language: Python v3.7
# Standard: PEP 8

'''
Author: Abhishek Singh
email: a.s.2013.hts@gmail.com
Copyright: (C) 2020 Abhishek Singh
License: GNU General Public License v3 (GPLv3) | see LICENSE for more details
Source Code: https://github.com/singh2505/bkliz | see README for more details

Contribution: Wanna contribute to bkliz library? | see CONTRIBUTING for more details
'''

import setuptools


with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="bkliz",
    version="1.0.3",
    author="Abhishek Singh",
    author_email="a.s.2013.hts@gmail.com",
    description="A Fast, Secure and Powerful Encryption library based on UTF - 8 Character Encoding.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/singh2505/bkliz",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
