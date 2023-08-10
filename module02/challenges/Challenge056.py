from emoji import emojize
from ClassColorsEmojis import *

print("{}{:=^50}{}".format(Color.greenBold, emojize(" CHALLENGE 056 " + Emoji.challenge), Color.reset))

print("""Develop a program that reads the name, age and gender of 4 people. At the end of the program,
show: the average age of the group, what is the name of the oldest man and how many women are under 20.""")

sumAge = 0
avgAge = 0
biggestAgeMan = 0
oldestMan = ""
totWomen20 = 0

for pearson in range (1,5):

    print("-"*25, f" PEARSON {pearson} ", "-"*25)
    name = str(input("Type here the name: ")).strip()
    age = int(input("Age: "))
    sex = str(input("sex M/F: ")).strip()
    sumAge += age

    if pearson == 1 and sex in 'Mm':
        biggestAgeMan = age
        oldestMan = name
    if sex in 'Mm' and age > biggestAgeMan:
        biggestAgeMan = age
        oldestMan = name
    if sex in 'Ff' and age == 20:
        totWomen20 += 1


avgAge = (sumAge / pearson )
print(f" The average of the ages  of the group is {avgAge}")
print(f" The oldest man is {oldestMan} and his age is {biggestAgeMan} ")
print(f" The total  of women less than 20 is {totWomen20} ")

print("{}{:=^50}{}".format(Color.redBold, emojize("CHALLENGE 056 END " + Emoji.challenge),Color.reset))