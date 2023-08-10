from ClassColorsEmojis import *
from emoji import emojize


print ("{}{:=^50}{}".format(Color.redBold,emojize("CHALLENGE 61 " + Emoji.challenge),Color.reset))
print(f"""\n{Color.cyan}Write a software that ask to the user the fist
number and the common differential number of a arithmetic progression of 10 positions
Use  while Structure {Color.reset}\n""")

count = 1

while True:
    try:
        number = int(input("Enter the 1st number of the Arithmetic Progression: "))
        dif = int(input("Type here the differential number of the Arithmetic Progression: "))
        break
    except ValueError:
        print(f"\n{Color.redBold}Invalid input.{Color.reset}")

print(f"\n{Color.yellowBold}The Arithmetic Progression between {number} and {dif} in range of 10 is: \n{Color.reset}")

while count <= 10:
    aritProgression = number + (count-1) * dif
    print(f"{Color.greenBold} {aritProgression} {Color.reset}" , end="-")
    count += 1


print ("\n{}{:=^50}{}".format(Color.redBold,emojize("CHALLENGE 61 END" + Emoji.challenge),Color.reset))