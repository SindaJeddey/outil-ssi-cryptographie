from Crypto.Cipher import DES3
from base64 import urlsafe_b64encode as b64e, urlsafe_b64decode as b64d
import os
from ..padding import pad, unpad
from Crypto.Protocol.KDF import PBKDF2
from Crypto.Hash import SHA512
from dotenv import load_dotenv

load_dotenv()
SALT = os.getenv('SALT')
initial_vector = os.urandom(DES3.block_size)
class DES3Cipher:

    def __init__(self, password, key_size):
        if key_size not in [8, 16, 24]:
            raise IOError("Key Size must be 8 bytes")
        key = PBKDF2(password, SALT, key_size, count=1000000, hmac_hash_module=SHA512)
        self.key = key

    def encrypt(self, message):
        message = (pad(message, DES3.block_size)).encode()
        cipher = DES3.new(self.key, DES3.MODE_CBC, initial_vector)
        cipher_text = cipher.encrypt(message)
        return b64e(cipher_text).decode()

    def decrypt(self, cipher_text):
        cipher = DES3.new(self.key, DES3.MODE_CBC, initial_vector)
        cipher_text = b64d(cipher_text)
        return unpad(cipher.decrypt(cipher_text).decode())
