from emoji import emojize
from ClassColorsEmojis import *

print(Color.green,"\n", " CHALLENGE 57 ".center(50, emojize(Emoji.axe)),"\n",Color.reset)

print(Color.cyan,f"""Develop a software that read the sex of a pearson, but only accept tha values
like M or F, in case if it is wrong ask again until the right value\n""",Color.reset)

sex = input("Type your sex: ").lower().strip()

while sex not in 'mf':

    print(f"{Color.redBold}invalid data!!{Color.reset}")
    sex = input("Please Type your sex: ")

print(f"{Color.greenBold}Information  stored{Color.reset}")
print(f"{Color.greenBold}done{Color.reset}")

print(Color.green,"\n", " CHALLENGE 57".center(50, emojize(Emoji.axe)),"\n",Color.reset)