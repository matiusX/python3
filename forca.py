import random


def import_secret_word():
    words = []
    with open("words.txt", "r") as file:
        for line in file:
            line = line.strip()
            words.append(line)
    random_word = random.randrange(0, len(words))
    secret_word = words[random_word].lower()
    return secret_word


def unknown_letters(unknown_word):
    return ['_' for letter in unknown_word]


def validate_chute():
    count = 0
    for letter in word:
        if letter == chute:
            letters[count] = letter
        count += 1


def winner_or_loser():
    if died:
        print('You lose!!')
        print('The word was {}'.format(word))
        print("  _______     ")
        print(" |/      |    ")
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")
        print(" |            ")
        print("_|___         ")
        print()
        print()
        print()
        print("    _______________         ")
        print("   /               \       ")
        print("  /                 \      ")
        print("//                   \/\  ")
        print("\|   XXXX     XXXX   | /   ")
        print(" |   XXXX     XXXX   |/     ")
        print(" |   XXX       XXX   |      ")
        print(" |                   |      ")
        print(" \__      XXX      __/     ")
        print("   |\     XXX     /|       ")
        print("   | |           | |        ")
        print("   | I I I I I I I |        ")
        print("   |  I I I I I I  |        ")
        print("   \_             _/       ")
        print("     \_         _/         ")
        print("       \_______/           ")
    else:
        print('You win!!')
        print(word)
        print("       ___________      ")
        print("      '._==_==_=_.'     ")
        print("      .-\\:      /-.    ")
        print("     | (|:.     |) |    ")
        print("      '-|:.     |-'     ")
        print("        \\::.    /      ")
        print("         '::. .'        ")
        print("           ) (          ")
        print("         _.' '._        ")
        print("        '-------'       ")


def desenha_forca(erros):
    print("  _______     ")
    print(" |/      |    ")

    if (erros == 6):
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if (erros == 5):
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    if (erros == 4):
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if (erros == 3):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if (erros == 2):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if (erros == 1):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")


word = import_secret_word()
letters = unknown_letters(word)

died = False
won = False
chances = 6
while not died and not won:
    formatted_letters = ' '.join(letters)

    print('playing!!')
    print(formatted_letters)

    chute = input("What's the letter?").lower().strip()

    if chute in word:
        validate_chute()
    else:
        desenha_forca(chances)
        chances -= 1
        print('You have {} chances yet'.format(chances))

    died = chances == 0
    won = '_' not in letters

winner_or_loser()







