from os import system, name
from symmteric_encryption.aes.aes import AESCipher
from symmteric_encryption.des.des import DESCipher
from symmteric_encryption.des.des3 import DES3Cipher
from getpass import getpass

def clear():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')

class SymmetricEncryption:
    def __repr__(self):
        menu = True
        print(
            '------------------------------------- Chiffrement/Déchiffrement Symétrique -------------------------------------\n'
            '1- Chiffrement symétrique\n'
            '2- Déchiffrement symétrique\n'
            '0- Retour au menu principal\n\n')

        while menu:
            choice = int(input('>>>  Option: '))
            clear()
            if choice not in [0, 1, 2]:
                print('! Choix non valide. Veuillez ré-essayer.\n>>>  ')

            elif choice == 0:
                clear()
                menu = False
                break

            elif choice == 1:
                sub_menu = True
                print(
                    '------------------------------------- Chiffrement Symétrique -------------------------------------\n'
                    '1- AES (Key size: 16, 24 or 32 bytes) \n'
                    '2- DES (Key size: 8 bytes) \n'
                    '3- Triple DES (Key size: 8, 16 or 24 bytes)\n'
                    '0- Retour au menu précédent\n\n')
                while sub_menu:
                    algorithm = int(input('>>>  Option: '))

                    if algorithm not in [0, 1, 2, 3]:
                        print('! Choix non valide. Veuillez ré-essayer.\n>>>  ')

                    elif algorithm == 0:
                        clear()
                        sub_menu = False
                        print(
                            '------------------------------------- Chiffrement/Déchiffrement Symétrique -------------------------------------\n'
                            '1- Chiffrement symétrique\n'
                            '2- Déchiffrement symétrique\n'
                            '0- Retour au menu principal\n\n')
                        break

                    else:
                        key_size = int(input('-- Key-Size: '))
                        passphrase = getpass(prompt='-- Passphrase: ')
                        if algorithm == 1:
                            cipher = AESCipher(passphrase, key_size)
                        elif algorithm == 2:
                            cipher = DESCipher(passphrase)
                        else:
                            cipher = DES3Cipher(passphrase, key_size)
                        message = input('-- Message à chiffrer: ')
                        result = cipher.encrypt(message)
                        print(f">>> Message chiffré: {result}\n\n")

            elif choice == 2:
                sub_menu = True
                print(
                    '------------------------------------- Déchiffrement Symétrique -------------------------------------\n'
                    '1- AES (Key size: 16, 24 or 32 bytes) \n'
                    '2- DES (Key size: 8 bytes) \n'
                    '3- Triple DES (Key size: 8, 16 or 24 bytes)\n'
                    '0- Retour au menu précédent\n\n')
                while sub_menu:
                    algorithm = int(input('>>>  Option: '))

                    if algorithm not in [0, 1, 2, 3]:
                        print('! Choix non valide. Veuillez ré-essayer.\n>>>  ')

                    elif algorithm == 0:
                        clear()
                        sub_menu = False
                        print(
                            '------------------------------------- Chiffrement/Déchiffrement Symétrique -------------------------------------\n'
                            '1- Chiffrement symétrique\n'
                            '2- Déchiffrement symétrique\n'
                            '0- Retour au menu principal\n\n')
                        break

                    else:
                        key_size = int(input('-- Key-Size: '))
                        passphrase = getpass(prompt='-- Passphrase: ')
                        if algorithm == 1:
                            cipher = AESCipher(passphrase, key_size)
                        elif algorithm == 2:
                            cipher = DESCipher(passphrase)
                        else:
                            cipher = DES3Cipher(passphrase, key_size)
                        message = input('-- Message à déchiffrer: ')
                        result = cipher.decrypt(message)
                        print(f">>> Message déchiffré: {result}\n\n")



