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
            print(f'{Color.redBold}Invalid input{Color.reset}')

def askContinue():
    while True:
        ask =  input(f'{Color.greenBold}Do you wanna continue? {Color.reset}').strip().upper()
        if ask[0] ==  'S':
            return True
        elif ask[0] ==  'N':
            return False
        else:
            print(f'{Color.redBold}Invalid input Try again{Color.reset}')


print(f'{Color.greenBold}How  many number you wanna enter{Color.reset}')
rangeInput = checkInput()

for entrance in range(0,rangeInput):
    number = checkInput()

    while True :
        if number not  in numbers:
            numbers.append(number)
            print(f'{Color.greenBold} Number successfully added{Color.reset}')
            break
        else:
            print(f'{Color.redBold} on the lis already have {number}. try other{Color.reset}')

        asw = askContinue()
        if not asw:
            break


print ("\n{}{:=^50}{}".format(Color.redBold,emojize("CHALLENGE 79 END" + Emoji.challenge),Color.reset))
