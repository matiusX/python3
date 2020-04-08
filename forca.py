word = 'apple'
letters = ['_', '_', '_', '_', '_']
'''
hello
'''
count_hits = 0
chances = 0

died = False
won = False
acertou = False

while not died and not won:
    count_letter = 0
    formatted_letters = ' '.join(letters)

    print('playing!!')
    print(formatted_letters)

    chute = input("What's the letter?")
    if chute in word:
        for letter in word:
            if letter.lower().strip() == chute.lower().strip():
                letters[count_letter] = letter
                count_hits += 1
                acertou = True

                if count_hits == len(letters):
                    won = True
                    print(word)
                    print('You win!!')
            count_letter += 1
    else:
        chances += 1
        if chances == 6:
            print('The word was: {}'.format(word))
            print('You lose!!')
            died = True




