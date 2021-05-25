# This is more of a “guess the word” game. The core concepts you have to use while developing this project
# are variables, random, integer, strings, char, input and output, and boolean. 
# In the game, users have to enter letter guesses, and each user will have a limited number of guesses 
# (a counter variable is needed for limiting the guesses). 
# This is one of the interesting python projects to begin with. 

# You can create a pre-organized list of words that users can grab words from. 
# Also, you must include specific functions to check whether or not a user has entered a single letter
# or if the input letter is in the hidden word, to if the user has actually inputted a single letter, 
# and to print the correct outcomes (letters).

import random

# sample word list, make longer to improve quality of game
word_list = ['king', 'queen', 'rook', 'bishop', 'knight', 'pawn']

def get_word():
    word = random.choice(word_list)
    return word.upper()

def play_game(word):
    word_display = '_' * len(word)
    guessed_letters = []
    guessed_words = []
    word_has_been_guessed = False
    attempts_remaining = 6
    print(word_display)

    while not word_has_been_guessed and attempts_remaining > 0:
        guess = input('Guess a letter or word: ').upper()
        # guessing a letter
        if len(guess) == 1 and guess.isalpha():
            if guess not in word:
                print(guess, 'is not in the word')
                attempts_remaining -= 1
                guessed_letters.append(guess)
            elif guess in guessed_letters:
                print('Letter has already been guessed.')
            else:
                print(guess, 'is in the word.')
                guessed_letters.append(guess)
                # iterate over the word by making it into a list and using the enumerate function
                # to replace the corresponding underscore(s) with the guessed letter
                word_as_list = list(word_display)
                indices = [i for i, letter in enumerate(word) if letter == guess]
                for index in indices:
                    word_as_list[index] = guess
                word_display = ''.join(word_as_list)
                if '_' not in word_display:
                    word_has_been_guessed = True

        # guessing a word
        elif len(guess) == len(word) and guess.isalpha():
            if guess != word:
                print(guess, 'is not the word.')
                guessed_words.append(guess)
                attempts_remaining -= 1
            elif guess in guessed_words:
                print(guess, 'has already been guessed.')
            else:
                word_has_been_guessed = True
                word_display = word

        else:
            print('Invalid guess.')
        
        print(word_display)

    if word_has_been_guessed:
        print('Congratulations! You guessed the word!')
    else:
        print('You ran out of attempts. The word was', word)

def main():
    word = get_word()
    play_game(word)
    while input('Play again? (Y/N): ').upper() == 'Y':
        word = get_word()
        play_game(word)

if __name__ == '__main__':
    main()