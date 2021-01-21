from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import dh
from cryptography.hazmat.primitives.kdf.hkdf import HKDF
from cryptography.hazmat.primitives import serialization
from base64 import urlsafe_b64encode as b64e, urlsafe_b64decode as b64d


class DiffieHellman:

    def __init__(self):
        self.parameters = None

    def __load_private_key_from_file(self, file_name):
        try:
            with open(f"{file_name}_priv.pem", "rb") as private_key_file:
                private_key = serialization.load_pem_private_key(
                    private_key_file.read(),
                    password=None
                )
                return private_key
        except FileNotFoundError as e:
            print(f">>> File {file_name} not found")

    def __load_public_key_from_file(self, file_name):
        try:
            with open(f"{file_name}_pub.pem", "rb") as public_key_file:
                public_key = serialization.load_pem_public_key(
                    public_key_file.read()
                )
                return public_key
        except FileNotFoundError as e:
            print(f">>> File {file_name} not found")

    def __load_key(self, file_name):
        try:
            with open(f"{file_name}.key", "r") as signature_file:
                key = b64d(signature_file.read())
                return key
        except FileNotFoundError as e:
            print(f">>> File {file_name} not found")

    def __save_key(self, key, file_name):
        key_file = open(f"{file_name}.key", "w+")
        key_file.write(b64e(key).decode())

    def generate_parameters(self, generator, key_size):
        try:
            self.parameters = dh.generate_parameters(generator, key_size)
        except ValueError as error:
            print(error)

    def generate_key_pair(self, key_name):
        private_key = self.parameters.generate_private_key()
        pem_private_key = private_key.private_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PrivateFormat.PKCS8,
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

    def generate_shared_key(self, peer1_private_key_file, peer2_public_key_file, key_name):
        peer1_private_key = self.__load_private_key_from_file(peer1_private_key_file)
        peer2_public_key = self.__load_public_key_from_file(peer2_public_key_file)
        shared_key = peer1_private_key.exchange(peer2_public_key)
        self.__save_key(shared_key, key_name)

    def generate_derived_key(self, shared_key_file, length, info, key_name):
        shared_key = self.__load_key(shared_key_file)
        try:
            derived_key = HKDF(
                algorithm=hashes.SHA256(),
                length=length,
                salt=None,
                info=info.encode()).derive(shared_key)
            self.__save_key(derived_key, key_name)
        except Exception as e:
            print(e)

