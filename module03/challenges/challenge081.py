from ClassColorsEmojis import *
from emoji import emojize

print ("{}{:=^50}{}".format(Color.redBold,emojize("CHALLENGE 80 " + Emoji.challenge),Color.reset))

print(f"""\n{Color.cyan}Create a program that will read several numbers and put them in a list.
After that show:
A) How many numbers were entered.
B) The list of values, sorted in descending order.
C) If the value 5 was typed and is or is not in the list.
{Color.reset}\n""")

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

numbers = []
while True:
    number = checkInput()
    numbers.append(number)
    ask = askContinue()

    if not ask:
        break

counter = len(numbers)
numbers.sort(reverse = True)


print(f'A) the quantity of numbers you entered was {counter}')
print(f'B) the reversed list is {numbers}')
if 5 in numbers:
    print (f'C)There is a number  in  the list and the  position of it is {numbers.index(5)+1}')
else:
    print (f'C)There is no number 5 in the list ')

print ("\n{}{:=^50}{}".format(Color.redBold,emojize("CHALLENGE 80 END" + Emoji.challenge),Color.reset))