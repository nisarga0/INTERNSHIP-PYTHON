

import random

def choose_word(word_list):
    return random.choice(word_list)
def play_hangman(word):
    print('Welcome to Hangman!')
    guessed_letters = set()
    incorrect_guesses = 0
    max_guesses = 6
    while incorrect_guesses < max_guesses:
        clue = get_clue(word, guessed_letters)
        print(clue)
        guess = input('Guess your letter: ').upper()
        if guess in guessed_letters:
            print('You already guessed that letter!')
        continue
    guessed_letters.add(guess)
    if guess in word:
        print('Correct!')
        if set(word) == guessed_letters: 
            print('Congratulations! You won!')
            return
        else:
            print('Incorrect!') 
            incorrect_guesses += 1
            guesses_left = max_guesses - incorrect_guesses
            print(f'You have {guesses_left} guesses left.')
            print('Sorry, you lost!')
            print(f'The word was "{word}"')
            def get_clue(word, guessed_letters):
                clue = ''
                for letter in word:
                    if letter in guessed_letters:
                        clue += letter + ' '
                    else:
                        clue += '_ '
                        return 
                    clue.strip()