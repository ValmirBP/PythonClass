
from datetime import date
from emoji import emojize
from ClassColorsEmojis import *

print ("{}{:=^50}{}".format(Color.redBold, emojize("CHALLENGE 52" + Emoji.challenge), Color.reset))

print(f"""{Color.blueBold}Write a software that ask to the user the birthday of 7 people and
show how many reached 18 years or more {Color.reset}""")

from datetime import date

actualYear = date.today().year
majority = 0
minority = 0

for i in range(1, 8):
    while True:
        try:
            birthday = int(input('Enter the birth year: '))
            break
        except ValueError:
            print(f'{Color.redBold}Invalid Input{Color.reset}')

    age = actualYear - birthday

    if age >= 21:
        majority += 1
    else:
        minority += 1

print(f"{Color.darkGrey}\nNumber of legal age people: {majority} {Color.reset}")
print(f"{Color.darkGrey}\nNumber of minors: {minority} {Color.reset}")

print (f'{Color.greenBold}\nIn total {majority} people reached the majority and {minority} are minority {Color.reset}')
print ("{}{:=^50}{}".format(Color.redBold, emojize("CHALLENGE 52 END" + Emoji.challenge), Color.reset))