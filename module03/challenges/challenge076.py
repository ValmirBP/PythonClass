from random import randint
from ClassColorsEmojis import *
from emoji import emojize

print ("{}{:=^50}{}".format(Color.redBold,emojize("CHALLENGE 75 " + Emoji.challenge),Color.reset))

print(f"""\n{Color.cyan} Develop a program that reads four values from the keyboard and stores
them in a tuple. At the end, show:
A) How many times did the value 9 appear.
B) In which position was entered the first value 3.
C) What were the even numbers.
{Color.reset}\n""")

numbers = ()
number = 0
evenEncountered = False

while number != 999:
    try:
        number = int(input(f'{Color.green} Enter a number: {Color.reset}'))
        numbers += (number,)
    except ValueError:
        print(f'{Color.greenBold}\nInvalid input {Color.reset}')

nineCounts = numbers.count(9)
print(f'{Color.greenBold}\nThe number 9 appears {nineCounts} times {Color.reset}')

try:
    pos = numbers.index(3) + 1
    if pos == 1:
        print(f'{Color.greenBold} \nthe number 3 is in {numbers.index(3) + 1}st position {Color.reset}')
    elif pos == 2:
        print(f'{Color.greenBold} \nthe number 3 is in {numbers.index(3) + 1}nd position {Color.reset}')
    elif pos == 3:
        print(f'{Color.greenBold} \nthe number 3 is in {numbers.index(3) + 1}rd position {Color.reset}')
    elif pos >= 4:
        print(f'{Color.greenBold} \nthe number 3 is in {numbers.index(3) + 1}th position {Color.reset}')
except ValueError:
    print(f'{Color.redBold}\nThere is no number 3 here{Color.reset}')

print(f'{Color.greenBold}\nEven numbers are: {Color.reset}', end= '')

for even in numbers:
    if even % 2 == 0:
        print(f'{Color.yellowBold}{even}{Color.reset}', end =' ')
        evenEncountered = True

if not evenEncountered:
    print(f'{Color.yellowBold}0{Color.reset}')

print ("\n{}{:=^50}{}".format(Color.redBold,emojize("CHALLENGE 75 END" + Emoji.challenge),Color.reset))
