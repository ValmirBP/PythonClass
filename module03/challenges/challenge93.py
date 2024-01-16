from ClassColorsEmojis import *
from emoji import emojize

print("{}{:=^50}{}".format(Color.redBold, emojize(" CHALLENGE 93 " + Emoji.challenge), Color.reset))

print(f"""\n{Color.cyan} Create a program that manages the performance of a football player.
      The program will read the player's name and how many games he has played.
      Then you will read the number of goals scored in each match. In the end, all of this will be
      stored in a dictionary, including the total number of goals scored during the championship.
{Color.reset}\n""")

playerName = input(f'{Color.lightBlue}gamer name{Color.reset}')
while True:
    try:
        games = int(input(f'{Color.lightBlue} games played{Color.reset}'))
        break
    except ValueError:
        print(f'{Color.red}invalid input!!!{Color.reset}')

championship = []
goals = []
game = 0
while game < games:
    goal = int(input(f'number of goals on game {game}: '))
    game += 1
    goals.append(goal)

gamesInfo = {
        'Name': playerName,
        'games': games,
        'goals': goals
    }
championship.append(gamesInfo)
print(championship)

print("\n{}{:=^50}{}".format(Color.redBold, emojize("CHALLENGE 93 END" + Emoji.challenge), Color.reset))
