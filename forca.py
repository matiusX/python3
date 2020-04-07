word = 'apple'
letters = ['_', '_', '_', '_', '_']

count_hits = 0

died = False
won = False
while not died and not won:
    count_letter = 0
    formatted_letters = ' '.join(letters)

    print('playing!!')
    print(formatted_letters)

    chute = input("What's the letter?")
    for letter in word:
        if letter.lower().strip() == chute.lower().strip():
            letters[count_letter] = letter
            count_hits += 1

            if count_hits == len(letters):
                won = True
                print(word)
                print('You win!!')
        count_letter += 1


