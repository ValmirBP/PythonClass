from ClassColorsEmojis import *
from emoji import emojize
from tabulate import tabulate

print ("{}{:=^50}{}".format(Color.redBold,emojize("CHALLENGE 78 " + Emoji.challenge),Color.reset))

print(f"""\n{Color.cyan}Write a program that reads 5 numerical values and stores them in a list.
At the end, show which was the largest and smallest value typed and their respective positions
in the list.
{Color.reset}\n""")

numbers = []
def checkNumber():
    while True:
        try:
            number = int(input('Enter a number: '))
            return number
        except ValueError:
            print(f'{Color.red}Invalid input. Please enter a valid number.{Color.reset}')

for number in  range (0,5):
    numInput =  checkNumber()
    numbers.append(numInput)
print(numbers)

print ("\n{}{:=^50}{}".format(Color.redBold,emojize("CHALLENGE 78 END" + Emoji.challenge),Color.reset))
