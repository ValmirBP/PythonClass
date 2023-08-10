from emoji import emoji_list, emojize
from ClassColorsEmojis import *

print ("{}{:=^50}{}".format(Color.redBold, emojize("CHALLENGE 50" + Emoji.challenge), Color.reset))

print(f"{Color.blueBold}Write a software that ask to the user 6 numbers AND sum only the pairs {Color.reset}")

s=0

for i in range (1,7):
    number = int(input("Type here a number: ").strip())
    if number%2 == 0 :
        s +=number
print(s)

print ("{}{:=^50}{}".format(Color.redBold, emojize("CHALLENGE 50 END" + Emoji.challenge), Color.reset))