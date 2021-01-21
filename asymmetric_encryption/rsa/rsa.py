from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding
from base64 import urlsafe_b64encode as b64e, urlsafe_b64decode as b64d
from cryptography.exceptions import InvalidSignature
import os

class RSA:

    def __load_private_key_from_file(self, file_name):
        try:
            with open(f"{file_name}_priv.pem", "rb") as private_key_file:
                private_key = serialization.load_pem_private_key(
                    private_key_file.read(),
                    password=None
                )
                return private_key
        except FileNotFoundError as e:
            print(f">>> File {file_name} not found\n")

    def __load_public_key_from_file(self, file_name):
        try:
            with open(f"{file_name}_pub.pem", "rb") as public_key_file:
                public_key = serialization.load_pem_public_key(
                    public_key_file.read()
                )
                return public_key
        except FileNotFoundError as e:
            print(f">>> File {file_name} not found\n")

    def __load_signature_from_file(self, file_name):
        try:
            with open(f"{file_name}.sig", "r") as signature_file:
                signature = b64d(signature_file.read())
                return signature
        except FileNotFoundError as e:
            print(f">>> File {file_name} not found\n")

    def generate_key_pair(self, key_size, key_name):
        if key_size % 2 == 1 or key_size < 512:
            raise IOError("Key size must be multiple of 2 and greater than 512")

        private_key = rsa.generate_private_key(
            public_exponent=65537,
            key_size=key_size
        )
        pem_private_key = private_key.private_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PrivateFormat.TraditionalOpenSSL,
            encryption_algorithm=serialization.NoEncryption()
        )
        private = open(f"{key_name}_priv.pem", "w+")
        private.write(pem_private_key.decode())

        public_key = private_key.public_key()
        pem_public_key = public_key.public_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PublicFormat.SubjectPublicKeyInfo
        )
        public = open(f"{key_name}_pub.pem", "w+")
        public.write(pem_public_key.decode())

    def sign_message(self, message, key_file, signature_name):
        private_key = self.__load_private_key_from_file(key_file)
        signature = private_key.sign(
            message.encode(),
            padding.PSS(
                mgf=padding.MGF1(hashes.SHA256()),
                salt_length=padding.PSS.MAX_LENGTH
            ),
            hashes.SHA256()
        )
        signature_file = open(f"{signature_name}.sig", "w+")
        signature_file.write(b64e(signature).decode())

    def verify_signature(self, message, signature_file_name, public_key_file):
        public_key = self.__load_public_key_from_file(public_key_file)
        signature = self.__load_signature_from_file(signature_file_name)
        try:
            public_key.verify(
                signature,
                message.encode(),
                padding.PSS(
                    mgf=padding.MGF1(hashes.SHA256()),
                    salt_length=padding.PSS.MAX_LENGTH
                ),
                hashes.SHA256()
            )
            print(">>>  Signature valide\n")
        except InvalidSignature as e:
            print(">>>  Signature non valide\n")

    def encrypt(self, message, public_key_file):
        public_key = self.__load_public_key_from_file(public_key_file)
        try:
            result = public_key.encrypt(
                message.encode(),
                padding.OAEP(
                    mgf=padding.MGF1(algorithm=hashes.SHA256()),
                    algorithm=hashes.SHA256(),
                    label=None
                )
            )
            return b64e(result).decode()
        except ValueError as error:
            print(error)

    def decrypt(self, encrypted_message, private_key_file):
        private_key = self.__load_private_key_from_file(private_key_file)
        decrypt = private_key.decrypt(
            b64d(encrypted_message.encode()),
            padding.OAEP(
                mgf=padding.MGF1(algorithm=hashes.SHA256()),
                algorithm=hashes.SHA256(),
                label=None
            )
        )
        return decrypt.decode()
