import random


def random_guess(x):
    random_num = random.randint(1,x)

    user_guess = 0
    while user_guess != random_num:
        user_guess = int(input(f"Guess a number between 1 to {x}: "))
        if user_guess > random_num:
            print("Incorrect,guess smaller number")
        elif user_guess < random_num:
            print("incorrect, please guess bigger number")
        else:
            print("Congrats, You are correct")

random_guess(100)