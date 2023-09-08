from ClassColorsEmojis import *
from emoji import emojize

print ("{}{:=^50}{}".format(Color.redBold,emojize("CHALLENGE 80 " + Emoji.challenge),Color.reset))

print(f"""\n{Color.cyan} Create a program that declares a 3×3 matrix and fills it with values read
from the keyboard. At the end, show the matrix on the screen, with the correct formatting
{Color.reset}\n""")

Matrix = [[0,0,0],[0,0,0],[0,0,0]]
def checkInput():
    while True:
        try:
            uInput = int(input(f'{Color.greenBold}Enter a number{Color.reset}: '))
            return uInput
        except ValueError:
            print(f'{Color.redBold}invalid input.{Color.reset}')

for l in range (3):
    for c in range (3):
        Matrix[l] [c] = checkInput()

for l in range (3):
    for c in range (3):
        print (f'[{Matrix [l] [c]}]',end='')
    print()

print ("\n{}{:=^50}{}".format(Color.redBold,emojize("CHALLENGE 80 END" + Emoji.challenge),Color.reset))
