from Crypto.Cipher import DES
from base64 import urlsafe_b64encode as b64e, urlsafe_b64decode as b64d
import os
from ..padding import pad, unpad
from Crypto.Protocol.KDF import PBKDF2
from Crypto.Hash import SHA512
from dotenv import load_dotenv

load_dotenv()
SALT = os.getenv('SALT')
initial_vector = os.urandom(DES.block_size)
class DESCipher:

    def __init__(self, password):
        key = PBKDF2(password, SALT, 8, count=1000000, hmac_hash_module=SHA512)
        self.key = key

    def encrypt(self, message):
        message = (pad(message, DES.block_size)).encode()
        cipher = DES.new(self.key, DES.MODE_CBC, initial_vector)
        cipher_text = cipher.encrypt(message)
        return b64e(cipher_text).decode()

    def decrypt(self, cipher_text):
        cipher = DES.new(self.key, DES.MODE_CBC, initial_vector)
        cipher_text = b64d(cipher_text)
        return unpad(cipher.decrypt(cipher_text).decode())
