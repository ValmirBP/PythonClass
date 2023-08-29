from random import randint
from ClassColorsEmojis import *
from emoji import emojize

print ("{}{:=^50}{}".format(Color.redBold,emojize("CHALLENGE 74 " + Emoji.challenge),Color.reset))

print(f"""\n{Color.cyan} Create a program that will generate five random numbers and put them in a
tuple. After that, show the list of generated numbers and also indicate the smallest and largest
values that are in the tuple.
{Color.reset}\n""")

randTuple = (randint(1,10),randint(1,10),randint(1,10),randint(1,10),randint(1,10))

print(f'Numbers generated',end=': ')
for number in randTuple:
    print(f'{Color.green} {number} {Color.reset}',end=' ')

print(f'{Color.greenBold}\n\nMax values generated is: {Color.yellowBold} {max(randTuple)} {Color.reset}')
print(f'{Color.greenBold}Min values generated is: {Color.yellowBold} {min(randTuple)} {Color.reset}')


print ("\n{}{:=^50}{}".format(Color.redBold,emojize("CHALLENGE 74 END" + Emoji.challenge),Color.reset))
