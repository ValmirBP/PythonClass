from ClassColorsEmojis import *
from emoji import emojize

print ("{}{:=^50}{}".format(Color.redBold,emojize("CHALLENGE 84 " + Emoji.challenge),Color.reset))

print(f"""\n{Color.cyan}Create a program where the user can enter seven numeric values and register
them in a single list that keeps even and odd values separate.
At the end, show the even and odd values in ascending order
{Color.reset}\n""")

even =[]
odd = []
numbers = []

def checkInput ():
    while True:
        try:
            userInput = int(input(f'{Color.greenBold}Enter a number{Color.reset}'))
            return userInput
        except ValueError:
            print(f'{Color.redBold}invalid input, please again.{Color.reset}')


for number in range(0,7):
    entrance = checkInput()
    numbers.append(entrance)

for number in numbers:
    if number % 2 ==0:
        even.append(number)
    else:
        odd.append(number)

if len(even) > 0 :
    even.sort()
    print(f'{Color.greenBold} the even numbers are : {even} {Color.reset}')
else:
    print(f'{Color.greenBold}There is no even number:{Color.reset}')

if len(odd) > 0 :
    odd.sort()
    print(f'{Color.greenBold} the odd numbers are : {odd} {Color.reset}')
else:
    print(f'{Color.greenBold} There is no odd number:{Color.reset}')

print ("\n{}{:=^50}{}".format(Color.redBold,emojize("CHALLENGE 84 END" + Emoji.challenge),Color.reset))
