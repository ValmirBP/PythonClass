from random import randint
from ClassColorsEmojis import *
from emoji import emojize


print ("{}{:=^50}{}".format(Color.redBold,emojize("CHALLENGE 68 " + Emoji.challenge),Color.reset))

print(f"""\n{Color.cyan}Create a program that plays even or odd with the computer. The game will
only stop when the player loses, displaying the total number of consecutive victories they
achieved at the end of the game.
{Color.reset}\n""")

lose = False
pcChoice = 0
result = 0
victories = 0
rightChoice = False


while not rightChoice:
    try:
        playerChoice = int(input(f'What do you want? [1] Even  [2] Odd: '))

        if playerChoice <= 0 or playerChoice > 2:
            print(f'{Color.red}Invalid input, Try again{Color.reset}')
        else:
            rightChoice = True

    except ValueError:
        print(f'{Color.red}Invalid input, Try again{Color.reset}')

if playerChoice == 1:
    pcChoice = 2
    print(f'PC {pcChoice} Odd, You {playerChoice} Even')
else:
    pcChoice = 1
    print(f'PC {pcChoice} Even, You {playerChoice} Odd')

while not lose:
    pc = randint(0,10)
    try:
        player = int(input(f'{Color.green}Enter a number between 0 and 10 {Color.reset}'))

        result = player + pc

        if player < 0 or player > 10:
            print(f'{Color.red}Invalid Range, Please enter a number between 0 and 10{Color.reset}')

        elif result % 2 == 0 and pcChoice == 2:
            print(f'PC Wins!')
            print(f'PC umber is {pc} your is {player} the result is {result}')
            lose = True

        elif result % 2 == 0 and playerChoice == 2:
            print(f'You Win!')
            print(f'PC umber is {pc} your is {player} the result is {result}')
            victories += 1

        elif result % 2 != 0 and pcChoice == 1:
            print(f'PC Wins!')
            print(f'PC umber is {pc} your is {player} the result is {result}')
            lose = True

        elif result % 2 != 0 and playerChoice == 1:
            print(f'PC umber is {pc} your is {player} the result is {result}')
            print(f'You Win!')
            victories += 1

    except ValueError:
        print(f'{Color.red}Invalid input, Try again{Color.reset}')

if victories > 1:
    print(f'You won {victories} times!! Congrats')
elif victories ==0:
    print(f'You Did not win any round Sorry!')
else:
    print(f'You won {victories} time!! Congrats')

print ("\n{}{:=^50}{}".format(Color.redBold,emojize("CHALLENGE 68 END" + Emoji.challenge),Color.reset))
