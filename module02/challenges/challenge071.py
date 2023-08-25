from random import randint
from ClassColorsEmojis import *
from emoji import emojize

print ("{}{:=^50}{}".format(Color.redBold,emojize("CHALLENGE 71 " + Emoji.challenge),Color.reset))

print(f"""\n{Color.cyan} Create a program that simulates the operation of an ATM.
At the beginning, ask the user what will be the amount to be withdrawn (integer number)
and the program will inform how many bills of each value will be delivered.
NOTE:
    Consider that the cashier has R$50, R$20, R$10 and R$1 bills.
{Color.reset}\n""")



print ("\n{}{:=^50}{}".format(Color.redBold,emojize("CHALLENGE 71 END" + Emoji.challenge),Color.reset))
