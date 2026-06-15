import random

def play_game():
    print("\n===== NUMBER GUESSING GAME =====")

    print("\nChoose Difficulty:")
    print("1. Easy (1-50)")
    print("2. Medium (1-100)")
    print("3. Hard (1-500)")

    choice = input("Enter choice: ")

    if choice == '1':
        limit = 50
        attempts_allowed = 10

    elif choice == '2':
        limit = 100
        attempts_allowed = 7

    elif choice == '3':
        limit = 500
        attempts_allowed = 5

    else:
        print("Invalid choice.")
        return

    secret_number = random.randint(1, limit)

    attempts = 0

    while attempts < attempts_allowed:
        try:
            guess = int(input(f"Guess a number between 1 and {limit}: "))
            attempts += 1

            if guess < secret_number:
                print("Too Low!")

            elif guess > secret_number:
                print("Too High!")

            else:
                score = attempts_allowed - attempts + 1
                print(f"Correct! You won with score: {score}")
                return

        except ValueError:
            print("Enter a valid number.")

    print(f"You Lost! The number was {secret_number}")

while True:
    play_game()

    again = input("\nPlay again? (yes/no): ").lower()

    if again != 'yes':
        print("Game Closed.")
        break