from hashing.hashage import Hashing
from encoding_decoding.encoding import Encoding
from symmteric_encryption.symmetric import SymmetricEncryption
from asymmetric_encryption.asymmetric import AsymmetricEncryption
from os import system, name

def clear():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')

def menu():
    menu = True
    while menu:
        print(
            '------------------------------- OUTIL SSI_INSAT POUR LA CRYPTOGRAPHIE -------------------------------\n\n'
            '1- Codage et décodage d\'un message\n'
            '2- Hashage d\'un message\n'
            '3- Craquage d\'un message haché\n'
            '4- Chiffrement et déchiffrement symétrique d\'un message\n'
            '5- Chiffrement et déchiffrement asymétrique d\'un message\n'
            '0- Quitter\n\n')
        x = int(input('>>>  Option: '))
        clear()
        if x == 1:
            encoding = Encoding()
            encoding.__repr__()
        if x == 2:
            hashing = Hashing("HASHING")
            hashing.__repr__()
        if x == 3:
            cracking = Hashing("CRACKING")
            cracking.__repr__()
        if x == 4:
            symmetric = SymmetricEncryption()
            symmetric.__repr__()
        if x == 5:
            asymmetric = AsymmetricEncryption()
            asymmetric.__repr__()
        elif x == 0:
            menu = False


if __name__ == '__main__':
    menu()
