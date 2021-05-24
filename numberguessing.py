# Make a program in which the computer randomly chooses a number between 1 to 10, 1 to 100, or any range. 
# Then give users a hint to guess the number. Every time the user guesses wrong, he gets another clue, 
# and his score gets reduced. The clue can be multiples, divisible, greater or smaller, or a combination of all.

import random

random_number = random.randint(1, 100)
score = 100
guess = None

while guess != random_number:
    guess = int(input("Guess a number between 1 and 100:"))
    if guess == random_number:
        print("You guessed the number. Your score is:" + str(score))
    elif guess > random_number:
        print("Your guess was too high. Try again.")
        score -= 10
        continue
    elif guess < random_number:
        print("Your guess was too low. Try again.")
        score -= 10
        continue

    if score == 0:
        print("You are bad at guessing. Your score is 0.")
        break