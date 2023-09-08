from ClassColorsEmojis import *
from emoji import emojize

print ("{}{:=^50}{}".format(Color.redBold,emojize("CHALLENGE 80 " + Emoji.challenge),Color.reset))

print(f"""\n{Color.cyan} Create a program where the user types any expression that uses parentheses.
Your application should analyze whether the passed expression has the open and closed parentheses
in the correct order.
{Color.reset}\n""")

expression = str(input(f'Type here the mathematic expression: '))

pile =[]
for symbol in expression:
    if symbol == '(':
        pile.append('(')
    elif symbol == ')':
        if len(pile) > 0:
            pile.pop()
        else:
            pile.append(')')
            break
if len(pile) == 0:
    print(f'{Color.greenBold}Math expression right{Color.reset}')
else:
    print(f'{Color.red}Math expression wrong{Color.reset}')

print ("\n{}{:=^50}{}".format(Color.redBold,emojize("CHALLENGE 80 END" + Emoji.challenge),Color.reset))
