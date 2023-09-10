from ClassColorsEmojis import *
from emoji import emojize

print ("{}{:=^50}{}".format(Color.redBold,emojize("CHALLENGE 87 " + Emoji.challenge),Color.reset))

print(f"""\n{Color.cyan} Improve the previous challenge by showing at the end:
A) The sum of all even values entered.
B) The sum of the values in the third column.
C) The largest value in the second line.
{Color.reset}\n""")


Matrix = [[0,0,0],[0,0,0],[0,0,0]]
evenSum = thirdCol = biggest = 0

def checkInput():
    while True:
        try:
            uInput = int(input(f'{Color.greenBold}Enter a number{Color.reset}: '))
            return uInput
        except ValueError:
            print(f'{Color.redBold}\nInvalid input.{Color.reset}')

for l in range(3): # built the Matrix
    for c in range(3):
        Matrix[l] [c] = checkInput()

print()

for l in range(3): # Format Matrix
    for c in range(3):
        print (f'{Color.yellowBold} [{Matrix [l] [c]}] {Color.reset}',end='')
    print()

print()

for l in range(3): # Sum all even numbers in Matrix
    for c in range(3):
        if  Matrix[l][c] % 2 == 0:
            evenSum += Matrix[l] [c]

print(f'{Color.greenBold}The sum of all even number is{Color.blue} {evenSum} {Color.reset}')

for l in range(3): # make the sum of numbers on third colum
    thirdCol += Matrix[l][2]

print(f'{Color.greenBold}The sum of numbers of third column is {Color.blue} {thirdCol} {Color.reset}')

for c in range(3):
    if c == 0:
        biggest = Matrix[1][c]
    elif Matrix[1][c] > biggest:
        biggest = Matrix[1][c]

print(f'{Color.greenBold}The sum of numbers of third column is{Color.blue} {biggest} {Color.reset}')

print ("\n{}{:=^50}{}".format(Color.redBold,emojize("CHALLENGE 87 END" + Emoji.challenge),Color.reset))
