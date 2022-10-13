#!/usr/bin/env python3
# Created by: Lia Duggan
# Created on: October 10th 2022
# This program has you guess the correct number
# between 0 and 9

import constants


def main():
    # Ask for Users Guess
    user_guess = int(input("Guess a number between 0 and 9:  "))
    print("")

    # Check if the guess is correct
    if user_guess == constants.correct_number:
        print("You guessed correctly!")
    # If guess isn't correct print you guessed wrong
    else:
        print("You guessed wrong")


if __name__ == "__main__":
    main()
