Bkliz |PyPi| |PyPI - Python Version| |GitHub| |PyPI - Format| |PyPI - Status|
=============================================================================

Bkliz (Black Lizard) is an Open Source Python Library for Encryption/Decryption. 
It is based on ``UTF - 8`` Character Encoding which provide unique
Encryption for same input over multiple iterations. It is:

-  **Fast:** It is build on Python 3 and work efficiently for long range
   inputs.
-  **Simple:** Its design makes it convenient and light weight.
-  **Secure:** It provide new encryption for same input again and again.
-  **Powerful:** It provide highly unbreakable encryption for each new
   input.
-  **Customizable:** You can add salt accordingly to increase its
   security.
-  **Open-Source:** You can modify its source code for your personal
   use.

Installation
------------

It is currently available for ``Python>=3.6`` and can be install using
``pip``:

    pip install -U bkliz

Example
-------

It provides two standard methods ``encode`` & ``decode`` which can be
used by importing bkliz library in your ``.py`` file:

.. code:: python

    import bkliz


    message = 'Meet me at 9 AM'

    for i in range(0,3):
        encode_mess = bkliz.encode(message)
        print('\nEnc/Mess: ' + encode_mess)

        decode_mess = bkliz.decode(encode_mess)
        print('Dec/Mess: ' + decode_mess)

Output:

::

    Enc/Mess: ¾ĀđČšiŁìùėÐ¨Wª»§uă=Xïèí¿v
    Dec/Mess: Meet me at 9 AM

    Enc/Mess: ©ë¦š±ćÀşvĜê§ìkPü ,±¯čċ^Ùu®
    Dec/Mess: Meet me at 9 AM

    Enc/Mess: ÁÓŚÔœėòhĵØzgŉ8}õÃõÁáÐÇP5ċ
    Dec/Mess: Meet me at 9 AM

Code of Conduct
---------------

Powflix has adopted "Contributor Covenant Code of Conduct V2.0",
participants are expected to follow the guidelines described in
`CODE\_OF\_CONDUCT <https://github.com/powflix/bkliz/blob/master/CODE_OF_CONDUCT.md>`__

Contributing
------------

Your help in making BKLIZ better will be highly appreciated. If you're
interested, please refer
`CONTRIBUTING <https://github.com/powflix/bkliz/blob/master/CONTRIBUTING.md>`__

License
-------

Bkliz is licensed under "GNU General Public License v3 (GPLv3)", read
details in
`LICENSE <https://github.com/powflix/bkliz/blob/master/LICENSE>`__

Copyright
---------

Copyright (C) 2020 Powflix Inc., and its affiliates \|
`Website <http://powflix.live>`__ \|
`GitHub <https://github.com/powflix>`__ \|
`Twitter <https://twitter.com/powflix>`__ \|

.. |PyPi| image:: https://img.shields.io/pypi/v/bkliz
   :target: https://pypi.org/project/bkliz
.. |PyPI - Python Version| image:: https://img.shields.io/pypi/pyversions/bkliz
   :target: https://pypi.org/project/bkliz
.. |GitHub| image:: https://img.shields.io/github/license/powflix/bkliz
   :target: https://github.com/powflix/bkliz/blob/master/LICENSE
.. |PyPI - Format| image:: https://img.shields.io/pypi/format/bkliz
   :target: https://pypi.org/project/bkliz
.. |PyPI - Status| image:: https://img.shields.io/pypi/status/bkliz
   :target: https://pypi.org/project/bkliz