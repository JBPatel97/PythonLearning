from words import word_list
import random

# class bcolors:
#     HEADER = '\033[95m'
#     OKBLUE = '\033[94m'
#     OKCYAN = '\033[96m'
#     OKGREEN = '\033[92m'
#     WARNING = '\033[93m'
#     FAIL = '\033[91m'
#     ENDC = '\033[0m'
#     BOLD = '\033[1m'
#     UNDERLINE = '\033[4m'

# print(f"{bcolors.WARNING}Warning: No active frommets remain. Continue?{bcolors.UNDERLINE}")

# print("\033[48;5;236m\033[38;5;231mStack \033[38;5;208mAbuse\033[0;0m")
# coloredword = ''
# word = split(input('Enter word: '))
# for i in word:
#     coloredword = coloredword + f"\033[38;5;208m{i}\033[0;0m"
# print(coloredword)


def split(word):
    return [char for char in word]


def checkword(word):
    while len(word) != 5:
        print('Only 5 characters allowed. Try again.')
        word = input('Guess word: ')
    return word

def compare(guess, word):
    displayword = ''
    for x, y in zip(guess, word):
        if x == y:
            displayword = displayword + f"\033[38;5;46m{x}\033[0;0m"
        elif x in word:
            displayword = displayword + f"\033[38;5;208m{x}\033[0;0m"
        else:
            displayword = displayword + x
    return displayword



attempt = 0
word = random.choice(word_list).lower()

guesses = list()
originalguess = ''
checkedguesses = ''
while attempt <= 5:
    displayword = ''
    while True:
        originalguess = checkword(input('Guess word: '))
        if originalguess in guesses:
            originalguess = print('You guessed that word before! Try again. ')
        else:
            break
    guesses.append(originalguess)
    guess = split(originalguess)
    displayword = compare(guess, word)
    attempt = attempt + 1
    checkedguesses = checkedguesses + '\n' + displayword
    print(checkedguesses)
    if originalguess == word:
        print(f'Congratulations, {originalguess} is correct!')
        break
print(f"The word was {word}")