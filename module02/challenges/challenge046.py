from time import sleep
from emoji import emojize
from ClassColorsEmojis import *


print("{}{:=^50}{}".format(Color.greenBold, emojize("CHALLENGE 46"+ Emoji.challenge), Color.reset))
print(f"{Color.cyan}Write a software the shows a countdown for a firework for the end of the year{Color.reset}")

for i in range (10,-1,-1):
    print(i)
    sleep(1)
print(" \nHappy new year!!!".upper() + emojize(":fireworks:"*10))
print("{}{:=^50}{}".format(Color.greenBold, emojize("CHALLENGE 46 END" + Emoji.challenge), Color.reset))