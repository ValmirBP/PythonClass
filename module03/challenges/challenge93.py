from ClassColorsEmojis import *
from emoji import emojize

print("{}{:=^50}{}".format(Color.redBold, emojize(" CHALLENGE 93 " + Emoji.challenge), Color.reset))

print(f"""\n{Color.cyan} Create a program that manages the performance of a football player.
      The program will read the player's name and how many games he has played.
      Then you will read the number of goals scored in each match. In the end, all of this will be
      stored in a dictionary, including the total number of goals scored during the championship.
{Color.reset}\n""")

playerName = input(f'{Color.lightBlue}Enter the player name: {Color.reset}')
championship = []
goals = []
game = 1  

while True:
    try:
        games = int(input(f'{Color.lightBlue}Enter the games played: {Color.reset}'))
        break
    except ValueError:
        print(f'{Color.red}Invalid input!!!{Color.reset}')

while game <= games:
    goal = int(input(f'Number of goals on game {game}: '))
    goals.append(goal)
    game += 1

gamesInfo = {
    'Name': playerName,
    'Games': games,
    'Goals': {f'Game {i + 1}': goals[i] for i in range(len(goals))},
    'Total Goals': sum(goals)
}

championship.append(gamesInfo)

# Print information line by line
print(f"\n{Color.yellow}Championship Information:{Color.reset}")
for info in championship:
    print(f"{Color.lightBlue}Player Name: {info['Name']}{Color.reset}")
    print(f"{Color.lightBlue}Games Played: {info['Games']}{Color.reset}")
    print(f"{Color.lightBlue}Goals by Game:")
    for game, goals in info['Goals'].items():
        print(f"  {game}: {goals} goals")
    print(f"{Color.lightBlue}Total Goals: {info['Total Goals']}{Color.reset}")

print("\n{}{:=^50}{}".format(Color.redBold, emojize("CHALLENGE 93 END" + Emoji.challenge), Color.reset))
