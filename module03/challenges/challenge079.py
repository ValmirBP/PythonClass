from ClassColorsEmojis import *
from emoji import emojize

print ("{}{:=^50}{}".format(Color.redBold,emojize("CHALLENGE 79 " + Emoji.challenge),Color.reset))

print(f"""\n{Color.cyan}Create a program where the user can type several numerical values and
register them in a list. If the number already exists there, it will not be added.
At the end, all unique values entered will be displayed, in ascending order.
{Color.reset}\n""")

numbers=[]

def checkInput():
    while True:
        try:
            userInput = int(input(f'{Color.greenBold}Enter a number: {Color.reset}'))
            return userInput
        except ValueError:
            print(f'{Color.redBold}\nInvalid input{Color.reset}')

print(f'{Color.greenBold}How  many number you wanna enter{Color.reset}')
rangeInput = checkInput()
print(f'{Color.greenBold}\nStarting list: {Color.reset}')

for entrance in range(0,rangeInput):
    while True :
        number = checkInput()
        if number not  in numbers:
            numbers.append(number)
            print(f'{Color.greenBold}\nNumber successfully added{Color.reset}')
            break
        else:
            print(f'{Color.redBold}\nOn the list already have {number}. try other number{Color.reset}')
numbers.sort()
print (f'the list added is:\n {numbers}',end=' ')

print ("\n{}{:=^50}{}".format(Color.redBold,emojize("CHALLENGE 79 END" + Emoji.challenge),Color.reset))
