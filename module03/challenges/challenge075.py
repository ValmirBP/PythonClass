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

print ("\n{}{:=^50}{}".format(Color.redBold,emojize("CHALLENGE 75 END" + Emoji.challenge),Color.reset))
