# Encoding: UTF-8
# Line Endings: LF(Unix)
# Programming Language: Python 3
# Syntax Standard: PEP 8


"""A Secure and Powerful Open Source Python Library for Encryption/Decryption.

Source: https://github.com/powflix/bkliz | see README for more details.
License: GNU General Public License v3 (GPLv3) | see LICENSE for more details.
Contribution: Wanna contribute to bkliz? | see CONTRIBUTING for more details.

Copyright (C) 2020 Powflix Inc., and its affiliates.
"""


import setuptools


with open("README.rst", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="bkliz",
    version="1.0.9",
    author="Powflix Inc.",
    author_email="Powflix@outlook.com",
    description="""A Secure and Powerful Open Source Python Library for
                    Encryption/Decryption.""",

    long_description=long_description,
    long_description_content_type="text/x-rst",
    url="https://github.com/powflix/bkliz",
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

    project_urls={
        "Bug Reports": "https://github.com/powflix/bkliz/issues",
        "Say Thanks!": "https://saythanks.io/to/powflix%40outlook.com",
        "Source": "https://github.com/powflix/bkliz/",
        "Documentation": "https://github.com/powflix/bkliz/blob/master/README.rst"
    },
)
