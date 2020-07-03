import os
import random
import sys

words = [ 'apple', 'banana', 'melon', 'coconut', 'grapes', 'pomegranate', 'mango', 'lemon', 'strawberry', 'lime', 'blueberry' ]


def clear():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system("cleat")

def draw(bad_guess, good_guess, secret_word):
    clear()

    print('Strikes: {}/7'.format(len(bad_guess)))
    print('')

    for letter in bad_guess:
        print(letter, end=' ')
    print('\n\n')
    
    for letter in secret_word:
        if letter in good_guess:
            print(letter, end='')
        else:
            print('_', end='')

    print('')

def get_guess(bad_guess, good_guess):
    while True:
        guess = input("Guess a letter: ").lower()

        if len(guess) != 1:
            print("You can only guess a single letter!")
            continue
        elif guess in bad_guess or guess in good_guess:
            print("You've already guess that letter")
            continue
        elif not guess.isalpha():
            print("You can nly guess letters")
            continue
        else:
            return guess


def play(done):
    clear()
    secret_word = random.choice(words)
    bad_guess = []
    good_guess = []

    while True:
        draw(bad_guess, good_guess, secret_word)
        guess = get_guess(bad_guess, good_guess)

        if guess in secret_word:
            good_guess.append(guess)
            foud = True
            for letter in secret_word:
              if letter not in good_guess:
                  found = False
            if found:
                print("You win")
                print("the word was {}".format(secret_word))
                done = True
        else:
            bad_guess.append(guess)
            if len(bad_guess) == 7:
              draw(bad_guess, good_guess, secret_word)
              print("You lost!")
              print("the word was {}".format(secret_word))
              done = True

        if done:
            play_agin = input("Play again? Y/n ").lower()
            if play_agin != 'n':
                return play(done= False)
            else:
                sys.exit()

def welcome():
    start = input("Press enter/return to start or Q to quit ").lower()
    if start == 'q':
        print('Bye!')
        sys.exit()
    else:
        return True
    
print("Welcome to letter guess")

done = False

while True:
    clear()
    welcome()
    play(done)
