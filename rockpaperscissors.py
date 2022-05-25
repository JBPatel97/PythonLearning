import random

choice = input("Rock (r), paper (p), or scissors (s)? ")
computer_choice = random.choice(["r", "p", "s"])

if choice != computer_choice:
    if choice == "r":
        if computer_choice == "p":
            print('Computer chose paper! You lose.')
        elif computer_choice == "s":
            print('Computer chose scissors! You win!')
    if choice == "p":
        if computer_choice == "s":
            print('Computer chose scissors! You lose.')
        elif computer_choice == "r":
            print('Computer chose rock! You win!')
    if choice == "s":
        if computer_choice == "r":
            print('Computer chose rock! You lose.')
        elif computer_choice == "p":
            print('Computer chose paper! You win!')
elif choice == computer_choice:
    print('Tie!')