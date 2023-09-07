from ClassColorsEmojis import *
from emoji import emojize

print ("{}{:=^50}{}".format(Color.redBold,emojize("CHALLENGE 80 " + Emoji.challenge),Color.reset))

print(f"""\n{Color.cyan} Create a program that will read several numbers and put them in a list.
After that, create two extra lists that will contain only the even and odd values entered,
respectively. At the end, show the contents of the three generated lists.
{Color.reset}\n""")
values = []
oddValues = []
evenValues = []

def checkInput():
    while True:
        try:
           number =  int(input(f'{Color.greenBold}Enter a number: {Color.reset}'))
           return number
        except ValueError:
            print(f'{Color.redBold}\ninvalid input{Color.reset}')

def askContinue ():
    while True:
        ask = input(f'{Color.greenBold}Do you want to continue? [Y]Yes [N]No {Color.reset}').strip().upper()
        if ask[0] == 'Y':
            return True
        if ask[0] == 'N':
            return False
        else:
            print(f'{Color.redBold}\nInvalid input, please enter Y or N{Color.reset}')

while True:
    number = checkInput()
    values.append(number)
    ask = askContinue()
    if not ask:
        break

for element in values:
    if element % 2  == 0:
        evenValues.append(element)
    else:
        oddValues.append(element)

values.sort()
oddValues.sort()
evenValues.sort()

print(f'{Color.blueBold}\nThe list of the values is {values} {Color.reset}',end='')
print(f'{Color.blueBold}\nThe list of the even values is {evenValues} {Color.reset}',end='')
print(f'{Color.blueBold}\nThe list of the odd values is {oddValues} {Color.reset}',end='')


print ("\n{}{:=^50}{}".format(Color.redBold,emojize("CHALLENGE 80 END" + Emoji.challenge),Color.reset))
