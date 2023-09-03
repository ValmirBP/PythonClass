from ClassColorsEmojis import *
from emoji import emojize

print ("{}{:=^50}{}".format(Color.redBold,emojize("CHALLENGE 80 " + Emoji.challenge),Color.reset))

print(f"""\n{Color.cyan}Create a program where the user can type five numerical values and register
them in a list, already in the correct insertion position (without using sort()). At the end,
show the sorted list on the screen.
{Color.reset}\n""")

numbers=[]

def checkInput():
    while True:
        try:
            userInput = int(input(f'{Color.greenBold}Enter a number: {Color.reset}'))
            return userInput
        except ValueError:
            print(f'{Color.redBold}\nInvalid input{Color.reset}')


for entrance in range(0,5):
    value  = checkInput()
    pos = 0
    while pos < len(numbers) and value > numbers[pos] :
        pos += 1
    numbers.insert(pos,value)
print(f'{Color.greenBold}\n ordered lis is {numbers} {Color.reset}',end=' ')



print ("\n{}{:=^50}{}".format(Color.redBold,emojize("CHALLENGE 80 END" + Emoji.challenge),Color.reset))
