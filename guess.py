import random

def guessing_game():
    # Generate a random number between 1 and 100
    number_to_guess = random.randint(1, 100)
    attempts = 0
    user_guess = None

    print("Welcome to the Number Guessing Game!")
    print("I have selected a number between 1 and 100. Can you guess what it is?")
    
    while user_guess != number_to_guess:
        try:
            # Get the user's guess and increment attempt counter
            user_guess = int(input("Enter your guess: "))
            attempts += 1

            if user_guess < number_to_guess:
                print("Too low! Try again.")
            elif user_guess > number_to_guess:
                print("Too high! Try again.")
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 100.")

    # Congratulate the user when they guess correctly
    print(f"Congratulations! You guessed the number {number_to_guess} in {attempts} attempts.")

# Start the game
if __name__ == "__main__":
    guessing_game()

