import random


def start_game():
    number = random.randint(1, 10)
    attempts = 0
    print("Welcome to the Guessing Game!")

    while attempts < 3:
        guess = int(
            input(f"Attempt {attempts + 1}/3 - Guess a number (1-10): "))
        attempts += 1

        if guess == number:
            print(f"You won in {attempts} attempts!")
            return
        else:
            print("Wrong guess!")

    print(f"Game Over! The number was {number}")


start_game()
