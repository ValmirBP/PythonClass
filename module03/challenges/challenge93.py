from ClassColorsEmojis import *
from emoji import emojize
import datetime

print ("{}{:=^50}{}".format(Color.redBold,emojize("CHALLENGE 92 " + Emoji.challenge),Color.reset))

print(f"""\n{Color.cyan} Create a program that reads name, year of birth and work card and registers
it (with age) in a dictionary. If by chance the CTPS is different from ZERO, the dictionary will
also receive the year of hire and salary. Calculate and add, in addition to age, how many years the
person will retire.
{Color.reset}\n""")


def checkCtps():
    while True:
        try:
            ctps = int(input('enter the CPTS number with no points or dashes')) # to do a validation  for number
        except ValueError:
            print(' error for CTPS')
        return ctps

def CheckDate():
    while True:
        try:
            birthday = input("Enter the birthday Date? (in MM/DD/YYYY) ")
            birthdate= datetime.datetime.strptime(birthday,"%m/%d/%Y").date()
            return birthdate
        except ValueError:
            print('time data does not match format MM/DD/YYYY')
        

while True :
    name = input(f'enter your name')
    birthdate  = CheckDate()
    Ctps = checkCtps()
    employees = list()

    employeeInfo ={
        'Name': name
        ,'CTPS': Ctps
        ,'Birthday date': birthdate}
    employees.append(employeeInfo)
    break

for employee, v in enumerate(employees):

print ("\n{}{:=^50}{}".format(Color.redBold,emojize("CHALLENGE 92 END" + Emoji.challenge),Color.reset))