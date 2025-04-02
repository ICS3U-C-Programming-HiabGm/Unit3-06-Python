# Created by: Hiab G
# Date: Wed, Feb. 28th
# This program creates a number guessing game where users try to guess a random number between (450, 9078)
import random


def main():
    # Generate a random number between 450 and 9078
    target_number = random.randint(450, 9078)

    # Get the player's guess
    try:
        player_guess = int(input("Guess the random number between 450-9078: "))
        if player_guess == target_number:
            print("You guessed correct!")
        else:
            print(
                f"You guessed wrong! The correct answer was: {target_number}")

    except Exception:
        player_guess = input("")
        print(
            f"Please enter a valid number, {player_guess} is not a valid number")


if __name__ == "__main__":
    main()
