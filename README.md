# Bkliz ![PyPi](https://img.shields.io/pypi/v/ng2django)  ![PyPI - License](https://img.shields.io/github/license/singh2505/bkliz) ![PyPI - Format](https://img.shields.io/pypi/format/Django) ![PyPI - Status](https://img.shields.io/pypi/status/Django) ![GitHub code size in bytes](https://img.shields.io/github/languages/code-size/singh2505/bkliz?color=yellow)

Bkliz (Black Lizard) is an Open Source Python library for Encryption/Decryption.
It is based on `UTF - 8` Character Encoding which provide unique Encryption for same input over iteration. It is:

* **Fast:** It is build on Python 3 and work efficiently for long range inputs.
* **Simple:** Its design makes it convenient and light weight.
* **Secure:** It provide new encryption for same input over again and again.
* **Powerful:** It provide highly unbreakable encryption for every input.
* **Customizable:** You can add salt accordingly to increase its security .
* **Open-Source:** You can modify its source code for your personal use.

## Installation
It is currently available for `Python>=3.6` and can be install using `pip`:
> pip install bkliz

## Example

It provides two standard methods `encode` & `decode` which can be used by importing bkliz library in your `.py` file:
```python
import bkliz

message = 'Meet me at 9 AM'

for i in range(0,3):
    encode_mess = bkliz.encode(message)
    print('\nEnc/Mess: ' + encode_mess)

    decode_mess = bkliz.decode(encode_mess)
    print('Dec/Mess: ' + decode_mess)

```
Output for above example:
```
Enc/Mess: ¾ĀđČšiŁìùėÐ¨Wª»§uă=Xïèí¿v
Dec/Mess: Meet me at 9 AM

Enc/Mess: ©ë¦š±ćÀşvĜê§ìkPü ,±¯čċ^Ùu®
Dec/Mess: Meet me at 9 AM

Enc/Mess: ÁÓŚÔœėòhĵØzgŉ8}õÃõÁáÐÇP5ċ
Dec/Mess: Meet me at 9 AM
```

## License

Bkliz is licensed under [GNU General Public License v3 (GPLv3)](./LICENSE)

## Contributing

Your help in making BKLIZ better will be highly appreciated. If you're interested, please read [CONTRIBUTING](./CONTRIBUTING)

## Copyright

Copyright (C) 2020 Abhishek Singh | [Github](https://github.com/singh2505) | [Twitter](https://twitter.com/real_singhaniya) | 
