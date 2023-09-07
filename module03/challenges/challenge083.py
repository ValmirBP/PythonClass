from ClassColorsEmojis import *
from emoji import emojize

print ("{}{:=^50}{}".format(Color.redBold,emojize("CHALLENGE 80 " + Emoji.challenge),Color.reset))

print(f"""\n{Color.cyan} Create a program where the user types any expression that uses parentheses.
Your application should analyze whether the passed expression has the open and closed parentheses
in the correct order.
{Color.reset}\n""")



print ("\n{}{:=^50}{}".format(Color.redBold,emojize("CHALLENGE 80 END" + Emoji.challenge),Color.reset))
