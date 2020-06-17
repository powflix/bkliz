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


import random


def encode(self):
    """Encryption Method of bkliz library."""
    storedkey = []
    storedmsg = ''

    for character in self:
        key = random.randint(33, 126)       # UTF - 8 Character Range

        storedmsg += chr(ord(character) + key)
        storedkey.append(key)

    for character in storedkey:
        storedmsg += chr(character + len(self))

    del(storedkey)      # Deleting the key generated for encryption

    return storedmsg


def decode(self):
    """Decryption Method of bkliz library."""
    storedkey = []
    storedmsg = ''
    counter = 0

    midpoint = int(len(self)/2)

    for character in self[midpoint:]:
        storedkey.append(ord(character) - midpoint)

    for character in self[0:midpoint]:
        storedmsg += chr(ord(character) - storedkey[counter])
        counter += 1

    del(storedkey)      # Deleting the key generated for decryption
    del(midpoint)       # Deleting temporary variable
    del(counter)        # Deleting temporary variable

    return storedmsg
