import base64
from typing import ValuesView
from Crypto.Cipher import AES
from Crypto.Hash import SHA256
from Crypto import Random

from django.conf import settings

class EncryptionManager (object):
    def __init__(self):
        super(EncryptionManager, self).__init__()
        self.key = str(settings.ENCRYPT_PATH_PASSPHRASE).encode("utf-8")

    def encrypt(self, value, encode=True):
        
        source = str.encode(value)
        key = SHA256.new(self.key).digest()
        
        IV = Random.new().read(AES.block_size)
        encryptor = AES.new(key, AES.MODE_CBC, IV)
        padding = AES.block_size - len(source) % AES.block_size 
        source += bytes([padding]) * padding 
        data = IV + encryptor.encrypt(source)

        return base64.b64encode(data).decode("latin-1") if encode else data

    def decrypt(self, value, decode=True):
        source = str(value)

        if decode: 
            source = base64.b64decode(source.encode("latin-1"))
        key = SHA256.new(self.key).digest()  
        IV = source[:AES.block_size]  
        decryptor = AES.new(key, AES.MODE_CBC, IV)
        data = decryptor.decrypt(source[AES.block_size:])
        padding = data[-1]  

        if data[-padding:] != bytes([padding]) * padding:  
            raise ValueError("Invalid padding...")

        return data[:-padding]  