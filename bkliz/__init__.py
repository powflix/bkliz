"""A Secure and Powerful Open Source Python Library for Encryption/Decryption.

Source: https://github.com/powflix/bkliz | see README for more details.
License: GNU General Public License v3 (GPLv3) | see LICENSE for more details.
Contribution: Wanna contribute to bkliz? | see CONTRIBUTING for more details.

Copyright (C) 2020 Powflix Inc., and its affiliates.
"""


from .bkliz import decode, encode

__all__ = ['__title__', '__version__', '__summary__', '__author__',
           '__email__', '__source__', '__license__', '__contribution__',
           '__copyright__', 'encode', 'decode']

try:
    import importlib.metadata

    metadata = importlib.metadata.metadata('bkliz')

    __title__ = metadata['name']
    __version__ = metadata['version']
    __summary__ = metadata['summary']
    __author__ = metadata['author']
    __email__ = metadata['author-email']
    __source__ = 'https://github.com/powflix/bkliz | see README for more details.'
    __license__ = 'GNU General Public License v3 (GPLv3) | see LICENSE for more details."'
    __contribution__ = 'Wanna contribute to bkliz? | see CONTRIBUTING for more details.'
    __copyright__ = 'Copyright (C) 2020 Powflix Inc., and its affiliates.'

except ImportError:
    import sys

    sys.stderr.write("""
        ==================================
        Bkliz Metadata ImportError Occured
        ==================================

        Bkliz's metadata is not imported, you can find it in your standard
        installation of python packages for your system account.

        //You can still use the standard methods of bkliz library.
    """)
