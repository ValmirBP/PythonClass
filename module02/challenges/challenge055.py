from emoji import emojize
from ClassColorsEmojis import *

print ("{}{:=^50}{}".format(Color.red, emojize("CHALLENGE 52"+ Emoji.challenge), Color.reset))

print(f"""{Color.blueBold}Write a software that ask to the user the weight
      of 5 people and check the biggest one{Color.reset}""")

fat = 0
thin = 0

for i in range (1,6):
    weight = float(input(f'type here the weight pearson {i}: '))
    if i ==1:
        fat= weight
        thin= weight
    else:
        if weight > fat:
            fat = weight
        if weight < thin:
            thin = weight

print(f'The biggest weight is {fat}Kg')
print(f'The smallest weight is {thin}Kg')

print ("{}{:=^50}{}".format(Color.redBold, emojize("CHALLENGE 52 END" + Emoji.challenge), Color.reset))