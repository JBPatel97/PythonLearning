import random
 
def guess(x):
    randomnumber = random.randint(1,x)
    guess = 0
    while guess != randomnumber:
        guess = int(input(f"Guess a random number between 1 and {x}: "))
        if guess > randomnumber:
            print("Your guess was too high!")
        elif guess < randomnumber:
            print("Your guess was too low!")
    print("Congratulations, you guessed the number!")


def computer_guess(x):
    low = 1
    high = x
    correctguess = "no"
    guess = random.randint(1,x)
    while correctguess == "no":
        correctguess = input(f"Is {guess} your number? (yes/no) ")
        if correctguess == "no":
            highlow = input("Is your number higher or lower? (higher/lower) ")
            if highlow == "higher":
                low = guess + 1
                guess = random.randint(low,high)
            elif highlow == "lower":
                high = guess - 1
                guess = random.randint(low,high)
    print(f"Your number is: {guess}!")

computer_guess(100)