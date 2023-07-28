from datetime import date
from emoji import emojize
from ClassColorsEmojis import *


print("{}{:=^50}{}".format(Color.greenBold, emojize("CHALLENGE 041",Emoji.challenge), Color.reset))

print(f"""{Color.red} Write a software that ask to the user the year of his birth and analyse the
categories of a swimming competition{Color.reset}\n""")

while True:
    try:
        birthYear = int(input("Type here your birth year: ").strip())
        break
    except ValueError:
        print(f"{Color.redBold}Invalid input. Please enter a valid year.{Color.reset}")

actualYear= date.today().year
age = actualYear - birthYear

if age == 9:
    stage = "Little"
    print(f"{Color.green}You are in category {stage} {Color.reset}\n")

elif age > 9 and age <= 14:
    stage = "childish"
    print(f"{Color.blue}You are in category {stage} {Color.reset}\n")

elif age > 14 and age <= 19:
    stage = "Junior"
    print(f"{Color.yellow}You are in category {stage} {Color.reset}\n")

elif age > 19 and age <= 20:
    stage = "Senior"
    print(f"{Color.blueBold}You are in category {stage} {Color.reset}\n")

elif age > 20:
    stage = "Master"
    print(f"{Color.yellowBold}You are in category {stage} {Color.reset}\n")

else:
    print(f"{Color.redBold}Sorry You are too young{Color.reset}")


print("{}{:=^50}{}".format(Color.greenBold, emojize("CHALLENGE 041 END", Emoji.challenge), Color.reset))