import hashlib
from os import system, name
from pathlib import Path

def clear():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')

# Wordlists are downloaded from hashes.org

wordlists = {
    1: open(Path(__file__).absolute().parent / "rockyou.txt", "rb"),
    2: open(Path(__file__).absolute().parent / "wordlist.txt", "rb")
}

algorithms = {
    1: hashlib.sha1,
    2: hashlib.sha256,
    3: hashlib.sha512,
    4: hashlib.md5
}


class Hashing:
    def __init__(self, operation):
        self.operation = operation

    def hashing(self, message, algo):
        return algorithms[algo](message.encode()).hexdigest()

    def cracking(self, hash, wordlist, algo):
        for i in wordlist.readlines():
            i = str(i, 'utf-8').rstrip("\n")
            word_hash = self.hashing(message=i, algo=algo)
            if word_hash == hash:
                return i
        return None

    def __repr__(self):
        menu = True
        if self.operation == "HASHING":
            print(
                '------------------------------------- Hashage -------------------------------------\n'
                '1- SHA-128\n'
                '2- SHA-256\n'
                '3- SHA-512\n'
                '4- MD5\n'
                '0- Retour au menu principal\n\n')
            while menu:
                x = int(input('>>>  Option: '))

                if x not in [0, 1, 2, 3, 4]:
                    print('! Choix non valide. Veuillez ré-essayer.\n>>>  ')

                elif x == 0:
                    clear()
                    menu = False
                    break

                else:
                    msg = input("-- Message à hasher: ")
                    hash = self.hashing(message=msg, algo=x)
                    print(f">>> Message hashé: {hash}\n\n")

        elif self.operation == "CRACKING":
            print(
                '------------------------------------- Craquage -------------------------------------\n'
                '1- Rock You wordlist\n'
                '2- MIT Wordlist\n'
                '0- Retour au menu principal\n')
            while menu:
                x = int(input('>>>  Option: '))

                if x not in [0, 1, 2]:
                    print('! Choix non valide. Veuillez ré-essayer.\n>>>  ')

                elif x == 0:
                    clear()
                    menu = False
                    break

                else:
                    wordlist = wordlists[x]
                    hash = input("-- Hashé à craquer: ")
                    print('\n>>> Veuillez choisir l\'algorithme de hashage:\n'
                          '1- SHA-128\n'
                          '2- SHA-256\n'
                          '3- SHA-512\n'
                          '4- MD5\n\n')
                    algo = int(input('>>>  '))

                    if algo not in [1, 2, 3, 4]:
                        print('! Choix non valide. Veuillez ré-essayer.\n>>>  ')

                    else:
                        result = self.cracking(hash=hash, wordlist=wordlist, algo=algo)
                        if result is None:
                            print('>>> Pas de mot trouvé!\n')
                        else:
                            print(f">>> Mot cracké: {result}")

