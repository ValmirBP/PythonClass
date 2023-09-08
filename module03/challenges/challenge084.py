from ClassColorsEmojis import *
from emoji import emojize

print ("{}{:=^50}{}".format(Color.redBold,emojize("CHALLENGE 80 " + Emoji.challenge),Color.reset))

print(f"""\n{Color.cyan} Make a program that reads the names and weights of several people,
saving everything in a list. At the end, show:
A) How many people were registered.
B) A list of the heaviest people.
C) A list of the lightest people.
{Color.reset}\n""")

people = list()
personInfo = list()
countPeople = 0

def checkWeight(name):
    while True:
        try:
            weight = float(input(f'{Color.greenBold}Enter the weight for {name}: {Color.reset}'))
            return weight
        except ValueError:
            print(f'{Color.redBold}invalid input for weight for {name}\nPlease try again {Color.reset}')

def askContinue():
    while True:
        ask =  input(f'{Color.greenBold}Do you want to continue? [Y]Yes [N]No {Color.reset}').strip().upper()
        if ask[0] == 'Y':
            return True
        elif ask[0] == 'N':
            return False
        else:
            print(f'{Color.redBold}Invalid answer {Color.reset}')

while True:
    name = input(f'{Color.greenBold}Enter a name: {Color.reset}')
    weight = checkWeight(name)
    personInfo.append(name)
    personInfo.append(weight)

    if len (people) == 0:
        lightest = heaviest = personInfo[1]
    else:
        if personInfo[1] > heaviest:
            heaviest = personInfo[1]
        if personInfo[1] < lightest:
            lightest = personInfo[1]

    people.append(personInfo[:])
    countPeople += 1
    personInfo.clear()
    ask = askContinue()

    if not ask:
        break

print(f'{Color.greenBold}\nA) the quantity entered is {countPeople}{Color.reset}')

print(f'{Color.greenBold}\nB) the Heaviest weight is {heaviest}KG. The names of them are: {Color.reset}',end=' ')
for w  in people:
    if w[1] == heaviest:
        print(f'{w[0]}',end=' ')

print(f'{Color.greenBold}\n\nC) the lightest weight is {lightest}KG. The names of them are: {Color.reset}',end=' ')
for w  in people:
    if w[1] == lightest:
        print(f'{w[0]}',end=' ')

print ("\n{}{:=^50}{}".format(Color.redBold,emojize("CHALLENGE 80 END" + Emoji.challenge),Color.reset))
