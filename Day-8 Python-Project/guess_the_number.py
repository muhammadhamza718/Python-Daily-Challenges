import random

def number_guessing_game():
    print("🎯 Welcome to the Number Guessing Game! 🔢")
    secret_number = random.randint(1, 100)
    attempts = 0

    while True:
        try:
            guess = int(input("Guess the number (between 1 and 100): "))
            attempts += 1

            if guess < 1 or guess > 100:
                print("⚠ Please enter a number between 1 and 100!")
            elif guess < secret_number:
                print("📉 Too low! Try again.")
            elif guess > secret_number:
                print("📈 Too high! Try again.")
            else:
                print(f"🎉 Congratulations! You guessed it right in {attempts} attempts! 🎯")
                break
        except ValueError:
            print("⚠ Invalid input! Please enter a valid number.")

if __name__ == "__main__":
    number_guessing_game()
