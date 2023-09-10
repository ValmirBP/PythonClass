from random import randint
from ClassColorsEmojis import *
from emoji import emojize

print ("{}{:=^50}{}".format(Color.redBold,emojize("CHALLENGE 88 " + Emoji.challenge),Color.reset))

print(f"""\n{Color.cyan}Write a program that helps a LOTO MAX player create predictions.
The program will ask how many games will be generated and will draw 6 numbers
between 1 and 60 for each game, registering everything in a composite list.
{Color.reset}\n""")

games = list()
singleGame = list()

def CheckImput():
    while True:
        try:
            uinput = int(input(f'{Color.green}Enter how many games you want to play {Color.reset}'))
            return uinput
        except ValueError:
            print(f'{Color.redBold}Invalid imput {Color.reset}')

def gameGen():
    count = 0
    while True:
        num = randint (1,60)
        if num not in singleGame:
            singleGame.append(num)
            count+=1
        if count >= 6 :
            games.append(singleGame[:])
            singleGame.clear()
            break

numGames = CheckImput()

for game in range(numGames):
    gameGen()

print(f'{Color.green}The games are: \n{Color.reset}')

for game in range(len(games)):
    print(f'{Color.yellowBold} {games[game]} {Color.reset}')

print ("\n{}{:=^50}{}".format(Color.redBold,emojize("CHALLENGE 88 END" + Emoji.challenge),Color.reset))
