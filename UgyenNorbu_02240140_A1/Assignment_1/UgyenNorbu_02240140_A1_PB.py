# Part B: Games

import random

def print_main_menu():
    print("\nSelect the Given Number to play a game :)")
    print("1. Guessing Number Game")
    print("2. Rock Paper Scissors Game")
    print("3. Exit program")

def guessing_number_game():
    number_to_guess = random.randint(1, 10)
    attempts = 0
    print("\nGuess the Number Game")

    while True:
        try:
            choose = int(input("Choose a number between 1 and 10: "))
            attempts += 1
            if choose < number_to_guess:
                print("The answer lies above... Try again!")
            elif choose > number_to_guess:
                print("You're close! Just go a bit lower.")
            else:
                print(f"Yes! That's the number! :) It took you {attempts} attempts.")
                break
        except ValueError:
            print("That doesn't seem right. Enter a valid number.")

def play_rock_paper_scissor():
    choices = ["rock", "paper", "scissor"]
    print("\nRock Paper Scissors Game")

    while True:
        select = input("Enter 'rock', 'paper', or 'scissor': ").lower()

        if select not in choices:
            print("Invalid choice! Please enter 'rock', 'paper', or 'scissor'.")
            continue

        computer_choice = random.choice(choices)
        print(f"Computer chose {computer_choice}.")

        if select == computer_choice:
            print("It's a tie! No one wins :)")
        elif (select == "rock" and computer_choice == "scissor") or \
             (select == "scissor" and computer_choice == "paper") or \
             (select == "paper" and computer_choice == "rock"):
            print("Congratulations, you won! :)")
        else:
            print("Better luck next time!")

        play_again = input("Do you want to play another round? (yes/no): ").lower()
        if play_again != "yes":
            break

def main():
    while True:
        print_main_menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            guessing_number_game()
        elif choice == '2':
            play_rock_paper_scissor()
        elif choice == '3':
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice! Please choose 1, 2, or 3.")

if __name__ == "__main__":
    main()
