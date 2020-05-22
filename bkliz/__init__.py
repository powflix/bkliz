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

from .bkliz import encode, decode


__all__ = ['__title__', '__version__', '__author__', '__email__', '__license__', '__copyright__', 'encode', 'decode',]

try:
    import importlib.metadata

    metadata = importlib.metadata.metadata('bkliz')

    __title__ = metadata['name']
    __version__ = metadata['version']
    __author__ = metadata['author']
    __email__ = metadata['author-email']
    __license__ = metadata['license']
    __copyright__ = 'Copyright (C) 2020 Abhishek Singh'

except:
    import sys
    print(sys.exc_info()[0])
