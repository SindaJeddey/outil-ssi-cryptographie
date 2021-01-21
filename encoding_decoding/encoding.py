import base64
from os import system, name

def clear():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')

class Encoding:
    def stringToBase64(self, string):
        return base64.b64encode(string.encode()).decode()

    def base64ToString(self, base):
        return base64.b64decode(base).decode()

    def __repr__(self):
        menu = True
        print(
            '------------------------------------- Codage/Decodage -------------------------------------\n'
            '1- Encoder en Base64\n'
            '2- Décoder Base64\n'
            '0- Retour au menu principal\n\n')
        while menu:

            choice = int(input('>>>  Option: '))

            if choice not in [0, 1, 2]:
                print('! Choix non valide. Veuillez ré-essayer.\n>>>  ')

            elif choice == 0:
                clear()
                menu = False
                break

            elif choice == 1:
                message = input("-- Message à encoder: ")
                result = self.stringToBase64(message)
                print(f">>> Message encodé: {result}\n\n")

            elif choice == 2:
                message = input("-- Message à décoder: ")
                result = self.base64ToString(message)
                print(f">>> Message décodé: {result}\n\n")
