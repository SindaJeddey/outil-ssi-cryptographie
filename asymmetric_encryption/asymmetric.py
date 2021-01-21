from os import system, name
from asymmetric_encryption.rsa.rsa import RSA
from asymmetric_encryption.dh.dh import DiffieHellman

def clear():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')

class AsymmetricEncryption:
    def __repr__(self):
        menu = True
        print(
            '------------------------------------- Chiffrement Asymétrique -------------------------------------\n'
            '1- RSA \n'
            '2- Diffie-Hellman \n'
            '0- Retour au menu précédent\n\n')
        while menu:
            algorithm = int(input('>>>  Option: '))

            if algorithm not in [0, 1, 2]:
                print('! Choix non valide. Veuillez ré-essayer.\n>>>  ')

            elif algorithm == 0:
                clear()
                menu = False
                break

            elif algorithm == 1:
                rsa_menu = True
                print(
                    '------------------------------------- RSA -------------------------------------\n'
                    '1- Générer une paire de clés \n'
                    '2- Signer un message \n'
                    '3- Vérifier une signature \n'
                    '4- Chiffrer un message \n'
                    '5- Déchiffrer un message \n'
                    '0- Retour au menu précédent\n\n')
                while rsa_menu:
                    rsa_choice = int(input('>>>  Option: '))
                    if rsa_choice not in [0, 1, 2, 3, 4, 5]:
                        print('! Choix non valide. Veuillez ré-essayer.\n>>>  ')
                    elif rsa_choice == 0:
                        system('clear')
                        rsa_menu = False
                        print(
                            '------------------------------------- Chiffrement Asymétrique -------------------------------------\n'
                            '1- RSA \n'
                            '2- Diffie-Hellman \n'
                            '0- Retour au menu précédent\n\n')
                        break
                    else:
                        rsa = RSA()
                        if rsa_choice == 1:
                            key_name = input("-- Nom des clé: ")
                            key_size = int(input("-- Taille des clé : "))
                            rsa.generate_key_pair(key_size, key_name)
                        elif rsa_choice == 2:
                            key_name = input("-- Nom de la clé privée: ")
                            signature_name = input("-- Nom de la signature : ")
                            message = input("-- Message à signer : ")
                            rsa.sign_message(message, key_name, signature_name)
                        elif rsa_choice == 3:
                            key_name = input("-- Nom de la clé publique: ")
                            signature_name = input("-- Nom de la signature : ")
                            message = input("-- Message à vérifier : ")
                            rsa.verify_signature(message, signature_name, key_name)
                        elif rsa_choice == 4:
                            key_name = input("-- Nom de la clé publique: ")
                            message = input("-- Message à chiffrer : ")
                            result = rsa.encrypt(message, key_name)
                            print(f">>> Message chiffré: {result}\n")
                        else:
                            key_name = input("-- Nom de la clé privée: ")
                            message = input("-- Message à déchiffrer : ")
                            result = rsa.decrypt(message, key_name)
                            print(f">>> Message déchiffré: {result}\n")
            elif algorithm == 2:
                dh_menu = True
                print(
                    '------------------------------------- Diffie-Hellman -------------------------------------\n'
                    '1- Générer une paire de clés \n'
                    '2- Générer une clé partagée \n'
                    '0- Retour au menu précédent\n\n')
                while dh_menu:
                    dh_choice = int(input('>>>  Option: '))

                    if dh_choice not in [0, 1, 2, 3, 4, 5]:
                        print('! Choix non valide. Veuillez ré-essayer.\n>>>  ')

                    elif dh_choice == 0:
                        clear()
                        dh_menu = False
                        print(
                            '------------------------------------- Chiffrement Asymétrique -------------------------------------\n'
                            '1- RSA \n'
                            '2- Diffie-Hellman \n'
                            '0- Retour au menu précédent\n\n')
                        break

                    else:
                        dh = DiffieHellman()
                        generator = int(input("-- Generateur: "))
                        key_size = int(input("-- Taille des clés: "))
                        dh.generate_parameters(generator, key_size)
                        if dh_choice == 1:
                            key_name = input("-- Nom des clé: ")
                            dh.generate_key_pair(key_name)
                        elif dh_choice == 2:
                            peer1_name = input("-- Nom de votre clé privée: ")
                            peer2_name = input("-- Nom de la clé publique du recepteur: ")
                            key_name = input("-- Nom de la clé partagée à générer : ")
                            dh.generate_shared_key(peer1_name, peer2_name, key_name)