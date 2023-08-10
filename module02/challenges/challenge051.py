from emoji import emoji_list, emojize
from ClassColorsEmojis import *


print ("{}{:=^50}{}".format(Color.redBold, emojize("CHALLENGE 51 " + Emoji.challenge), Color.reset))

print(f"""{Color.blueBold}Write a software that ask to the user the fist
number and the common differential number of a arithmetic progression of 10 positions {Color.reset}""")

while True :
    try:
        number = int(input("type here the 1st number of the Arithmetic Progression: "))
        dif = int(input("Type here the differential number of the Arithmetic Progression: "))
        break
    except ValueError:
        print(f"{Color.redBold}Invalid input{Color.reset}")

print(f"The Arithmetic Progression between {number} and {dif} in range of 10 is")

for  i in range (1,11):
    aritProgression = number + (i-1) * dif
    print(aritProgression, end=" ")

print ("\n{}{:=^50}{}".format(Color.redBold, emojize("CHALLENGE 51 END" + Emoji.challenge), Color.reset))