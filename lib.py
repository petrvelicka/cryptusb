import os

from cryptography.fernet import Fernet


class Crypto:
    def __init__(self, key_path):
        if os.path.exists(key_path):
            with open(key_path, 'rb') as file_key:
                self._key = Fernet(file_key.read())
        else:
            generated_key = self.generate_key(key_path)

            self._key = Fernet(generated_key)

    def generate_key(self, path):
        key = Fernet.generate_key()
        with open(path, "wb") as key_file:
            key_file.write(key)
        return key

    def encrypt(self, data):
        return self._key.encrypt(data)

    def decrypt(self, data):
        return self._key.decrypt(data)

    def encrypt_file(self, inf, outf):
        with open(inf, "rb") as file:
            # read the encrypted data
            data = file.read()
        enc_data = self.encrypt(data)
        with open(outf, "wb") as file:
            file.write(enc_data)

    def decrypt_file(self, inf, outf):
        with open(inf, "rb") as file:
            # read the encrypted data
            data = file.read()
        enc_data = self.decrypt(data)
        with open(outf, "wb") as file:
            file.write(enc_data)
