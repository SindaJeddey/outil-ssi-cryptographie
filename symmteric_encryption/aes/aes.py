from Crypto.Cipher import AES
from base64 import urlsafe_b64encode as b64e, urlsafe_b64decode as b64d
import os
from ..padding import pad, unpad
from Crypto.Protocol.KDF import PBKDF2
from Crypto.Hash import SHA512
from dotenv import load_dotenv

load_dotenv()
SALT = os.getenv('SALT')
initial_vector = os.urandom(AES.block_size)
class AESCipher:

    def __init__(self, password, key_size):
        if key_size not in [16, 24, 32]:
            raise IOError("Key Size must be 16, 24 or 32 bytes")
        key = PBKDF2(password, SALT, key_size, count=1000000, hmac_hash_module=SHA512)
        self.key = key

    def encrypt(self, message):
        message = (pad(message, AES.block_size)).encode()
        cipher = AES.new(self.key, AES.MODE_CBC, initial_vector)
        cipher_text = cipher.encrypt(message)
        return b64e(cipher_text).decode()

    def decrypt(self, cipher_text):
        cipher = AES.new(self.key, AES.MODE_CBC, initial_vector)
        cipher_text = b64d(cipher_text)
        return unpad(cipher.decrypt(cipher_text).decode())
