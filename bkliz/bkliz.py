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

import random


def encode(self):
    storedkey = []
    storedmsg = ''

    for character in self:
        key = random.randint(0,255)

        storedmsg+= chr(ord(character) + key)
        storedkey.append(key)

    for character in storedkey:
        storedmsg+= chr(character + len(self))

    del(storedkey)

    return storedmsg


def decode(self):
    storedkey = []
    storedmsg = ''
    counter = 0

    midpoint = int(len(self)/2)

    for character in self[midpoint:]:
        storedkey.append(ord(character) - midpoint)

    for character in self[0:midpoint]:
        storedmsg+= chr(ord(character) - storedkey[counter])
        counter+= 1

    del(storedkey)
    del(midpoint)

    return storedmsg
