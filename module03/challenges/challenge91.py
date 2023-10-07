from time import sleep
from operator import itemgetter
from random import randint
from ClassColorsEmojis import *
from emoji import emojize

print ("{}{:=^50}{}".format(Color.redBold,emojize("CHALLENGE 91 " + Emoji.challenge),Color.reset))

print(f"""\n{Color.cyan} Create a program where 4 players roll a dice and have random results.
Store these results in a dictionary in Python. At the end, put this dictionary in order,
knowing that the winner rolled the highest number on the dice.
{Color.reset}\n""")

game = {
    "player 1": randint(1, 6),
    "player 2": randint(1, 6),
    "player 3": randint(1, 6),
    "player 4": randint(1, 6)
}
sortedGame = list()
print("Dice rolls:")
for k, v in game.items():
    print(f'{k} got {v} on dice')

sortedGame = sorted(game.items(), key=itemgetter(1), reverse=True)

print("\nSorted rankings:")
print(sortedGame)
for  i,v in enumerate(sortedGame):
    if i == 1:
        print(f'{i+1}st place: {v[0]} got {v[1]}.')
    elif i ==2:
        print(f'{i+1}nd place: {v[0]} got {v[1]}.')
    elif i ==3:
        print(f'{i+1}rd place: {v[0]} got {v[1]}.')
    else:
        print(f'{i+1}th place: {v[0]} got {v[1]}.')


print ("\n{}{:=^50}{}".format(Color.redBold,emojize("CHALLENGE 91 END" + Emoji.challenge),Color.reset))
