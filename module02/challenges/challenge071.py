from random import randint
from ClassColorsEmojis import *
from emoji import emojize

print ("{}{:=^50}{}".format(Color.redBold,emojize("CHALLENGE 71 " + Emoji.challenge),Color.reset))

print(f"""\n{Color.cyan} Create a program that simulates the operation of an ATM.
At the beginning, ask the user what will be the amount to be withdrawn (integer number)
and the program will inform how many bills of each value will be delivered.
NOTE:
    Consider that the cashier has R$50, R$20, R$10 and R$1 bills.
{Color.reset}\n""")

value = int(input(f'what is the value for withdrawn: $ '))
total = value
moneyNotes = 50
totalMonNotes = 0


while True:
    if total >= moneyNotes:
            total -= moneyNotes
            totalMonNotes += 1
    else:
        if totalMonNotes > 0 :
            print(f'Total of {totalMonNotes} money notes of $ {moneyNotes}')
        if moneyNotes == 50:
            moneyNotes = 20

        elif moneyNotes == 20:
            moneyNotes = 10

        elif moneyNotes == 10:
            moneyNotes = 1

        totalMonNotes = 0
        if total == 0:
            break

print ("\n{}{:=^50}{}".format(Color.redBold,emojize("CHALLENGE 71 END" + Emoji.challenge),Color.reset))
