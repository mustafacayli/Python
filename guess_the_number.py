 

import random
logo="""
 _______                               _______ __               _______                  __               
|     __|.--.--.-----.-----.-----.    |_     _|  |--.-----.    |    |  |.--.--.--------.|  |--.-----.----.
|    |  ||  |  |  -__|__ --|__ --|      |   | |     |  -__|    |       ||  |  |        ||  _  |  -__|   _|
|_______||_____|_____|_____|_____|      |___| |__|__|_____|    |__|____||_____|__|__|__||_____|_____|__|  
                                                                                                          
"""

EASY_LEVEL = 10
HARD_LEVEL = 5


def check_answer(choosen_num, guess, turns):
    
    if guess > choosen_num:
        print(f"Too high")
        return turns - 1
    elif guess < choosen_num:
        print(f"Too low")
        return turns - 1
    else:
        print(f"You win guess is correct {choosen_num}")



def set_difficulty():
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard'\n")
    if difficulty.lower() == "easy":
        return EASY_LEVEL
    else:
        return HARD_LEVEL


def game():
    print("Welcome to the Number Guessing Game!")
    print("I am thinking of a number between 1 and 100")


    numbers = []
    for i in range(1,101):
        numbers.append(i)
    print(logo)
    choosen_num = random.choice(numbers)
    print(f"  {choosen_num}  ")


    turns = set_difficulty()
    guess = 0
    
    while guess != choosen_num: 

        print(f"\n\nYou have {turns} attempts reamaining to guess the number")
        guess = int(input(f"Guess the number between the 1 and 100\n"))
        turns = check_answer(guess,choosen_num, turns)
        if turns == 0:
            print("You've run out of guesses, you lose")
            return
        elif guess != choosen_num :
            print("Gues again.")

game()