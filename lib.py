import os

from cryptography.fernet import Fernet


class Crypto:
    def __init__(self, key=None):
        if not key:
            key = self.key_create()
        self._key = key

    def key_create(self):
        key = Fernet.generate_key()
        return key

    def key(self):
        return self._key

    def encrypt(self, data):
        f = Fernet(self._key)
        return f.encrypt(data)

    def decrypt(self, data):
        f = Fernet(self._key)
        return f.decrypt(data)

    def encrypt_file(self, inf, outf=None):
        with open(inf, "rb") as file:
            # read the encrypted data
            data = file.read()
        enc_data = self.encrypt(data)
        if not outf:
            return enc_data
        with open(outf, "wb") as file:
            file.write(enc_data)

    def decrypt_file(self, inf, outf=None):
        with open(inf, "rb") as file:
            # read the encrypted data
            data = file.read()
        dec_data = self.decrypt(data)
        if not outf:
            return dec_data
        with open(outf, "wb") as file:
            file.write(dec_data)
