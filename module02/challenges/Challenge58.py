from random import randint
from emoji import emojize


class color:
    black = '\033[30m'
    red = '\033[31m'
    green = '\033[32m'
    orange = '\033[33m'
    blue = '\033[34m'
    purple = '\033[35m'
    cyan = '\033[36m'
    lightGrey = '\033[37m'
    darkGrey = '\033[90m'
    lightRed = '\033[91m'
    lightGreen = '\033[92m'
    yellow = '\033[93m'
    lightBlue = '\033[94m'
    pink = '\033[95m'
    lightCyan = '\033[96m'
    reset = '\033[0m'

print(color.green, "\n"," CHALLENGE 58 ".center(50, emojize(":axe:")),color.reset, "\n")

print(color.cyan,"Improve the CHALLENGE 028 whe you  need to guess the number between 0 and 10, but the gamer need do the right guess  to end  the game ", color.reset)

number = randint(0,10)
guess = 0
name = input("Type here your name: ")
tries = 0
print(color.green,"Try to  guess the number", color.reset)

while guess != number:
    tries += 1
    try:
    guess = int(input("\n Type here he number: "))

    if guess == str(guess):
        print(color.red,"invalid value", color.reset)
    elif guess < number:
        print(color.red,"Sorry wrong guess. Try something BIGGER", color.reset)
    else:
        print(color.red,"Sorry wrong guess. Try something SMALLER", color.reset)
except ValueError:
    print("Please input a number.")**

print(color.green,f"congratulations!!! {name}, you got it with {tries}")



print(color.green, "\n"," CHALLENGE 58 ".center(50, emojize(":axe:")),color.reset, "\n")