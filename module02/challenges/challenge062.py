from ClassColorsEmojis import *
from emoji import emojize


print ("{}{:=^50}{}".format(Color.redBold,emojize("CHALLENGE 62 " + Emoji.challenge),Color.reset))
print(f"""\n{Color.cyan}Write a software that ask to the user the fist
number and the common differential number of a arithmetic progression of 10 positions
Use  while Structure and then ask to user  if there necessity to do more, to finish it, the user
must use enter 0 {Color.reset}\n""")

count = 1
total = 0
inputMore = 10

while True:
    try:
        number = int(input("Enter the 1st number of the Arithmetic Progression: "))
        dif = int(input("Type here the differential number of the Arithmetic Progression: "))
        break
    except ValueError:
        print(f"\n{Color.redBold}Invalid input.{Color.reset}")

print(f"\n{Color.yellowBold}The Arithmetic Progression between {number} and {dif} in range of 10 is: \n{Color.reset}")

while inputMore != 0:
    total += inputMore
    while count <= total:
        aritProgression = number + (count-1) * dif
        print(f"{Color.greenBold} {aritProgression} {Color.reset}" , end="-")
        count += 1

    print(f'{Color.greenBold}PAUSE{Color.reset}\n')

    while True:
        try:
            inputMore = int(input('How much differential you want to keep going on this AP? '))
            break
        except ValueError:
            print(f"\n{Color.redBold}Invalid input.{Color.reset}")


print(f'{Color.greenBold}END{Color.reset}')

print ("\n{}{:=^50}{}".format(Color.redBold,emojize("CHALLENGE 62 END" + Emoji.challenge),Color.reset))