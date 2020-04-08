import random

words = []
with open("words.txt", "r") as file:
    for line in file:
        line = line.strip()
        words.append(line)
random_word = random.randrange(0, len(words))

word = words[random_word].lower()
letters = ['_' for letter in word]

died = False
won = False
chances = 6
while not died and not won:
    count_letter = 0
    formatted_letters = ' '.join(letters)

    print('playing!!')
    print(formatted_letters)

    chute = input("What's the letter?").lower().strip()
    if chute in word:
        for letter in word:
            if letter == chute:
                letters[count_letter] = letter
            count_letter += 1
    else:
        chances -= 1
        print('You have {} chances yet'.format(chances))

    died = chances == 0
    won = '_' not in letters

if died:
    print('You lose!!')
    print('The word was {}'.format(word))
else:
    print('You win!!')
    print(word)






