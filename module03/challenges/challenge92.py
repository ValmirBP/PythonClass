from ClassColorsEmojis import *
from datetime import datetime
from emoji import emojize

print("{}{:=^50}{}".format(Color.redBold, emojize(" CHALLENGE 92 " + Emoji.challenge), Color.reset))

print(f"""\n{Color.cyan} Create a program that reads name, year of birth and work card and registers
it (with age) in a dictionary. If by chance the CTPS is different from ZERO, the dictionary will
also receive the year of hire and salary. Calculate and add, in addition to age, how many years the
person will retire.
{Color.reset}\n""")

flag = ""

def CheckDate():
    while True:
        try:
            birthYear = input(f'{Color.greenBold}Enter the birth year : {Color.reset}')
            if len(birthYear) == 4 :
                return int(birthYear)
            else:
                print(f'{Color.redBold}Invalid input, please enter a valid birth year (yyyy format).{Color.reset}')
        except ValueError:
            print(f'{Color.redBold}Invalid input, please enter numbers only.{Color.reset}')

def CheckRetireDate():
    while True:
        contract = input(f'{Color.greenBold}Enter the contract year : {Color.reset}')
        try:
            if len(contract) == 4:
                return int(contract)
            else:
                print(f'{Color.redBold}Invalid input, please enter a valid contract year (yyyy format).{Color.reset}')
        except ValueError:
            print(f'{Color.redBold}Invalid input, please enter numbers only.{Color.reset}')


def checkCPTS():
    while True:
        CPTSNumber = input(f'{Color.greenBold}Enter CPTS number only: {Color.reset}')
        try:
            if len(CPTSNumber) == 5:
                return int(CPTSNumber)
            else:
                print(f'{Color.redBold}Invalid input, does not correspond with CPTS number.{Color.reset}')
        except ValueError:
            print(f'{Color.redBold}Invalid input, please enter numbers only.{Color.reset}')

def continueFlag():
    print(f'{Color.greenBold}Want to continue? yes[Y] No[N] (Default yes) {Color.reset}')
    flag = input()
    return flag[0].lower()

employees = []

while flag != "n":
    today = datetime.now().year
    name = input(f'Enter your name: ')
    age =  CheckDate()
    retire = CheckRetireDate()

    employeeInfo = {
        'Name': name,
        'CTPS': checkCPTS(),
        'Age': today - age,
        'remaining to retire':  (retire + 35) - today
    }
    employees.append(employeeInfo)
    flag = continueFlag()

print(employees)

print("\n{}{:=^50}{}".format(Color.redBold, emojize("CHALLENGE 92 END" + Emoji.challenge), Color.reset))
