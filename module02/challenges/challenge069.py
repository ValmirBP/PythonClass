from random import randint
from ClassColorsEmojis import *
from emoji import emojize


print ("{}{:=^50}{}".format(Color.redBold,emojize("CHALLENGE 69 " + Emoji.challenge),Color.reset))

print(f"""\n{Color.cyan}Create a program that reads the age and gender of multiple people.
For each registered person, the program should ask if the user wants to continue or not.
In the end, show it.
{Color.reset}\n""")

def askContinue():
    while True:
        answer = input('Do you want to continue? [Y] Yes [N] No ').strip().upper()
        if answer == 'Y':
            print('OK!!')
            return True
        elif answer == 'N':
            return False
        else:
            print('Invalid input')

def validateAge():
    while True:
        try:
            age = int(input('Enter your age: '))
            if age < 0:
                print('Invalid Age: Age cannot be negative. Please try again.')
            else:
                return age
        except ValueError:
            print('Invalid Age: Please enter a valid number for age')

def validateGender():
    while True:
        gender = input('Enter your Gender [M] Male [F] Female [O] Other: ').strip().upper()
        if gender in ['F', 'M', 'O']:
            return gender
        else:
            print('Invalid Gender: Please enter [M] for Male, [F] for Female, or [O] for Other')

while True:
    try:
        age = validateAge()
        sex = validateGender()

        print(f'Age is: {age}, Gender is: {sex}')

        if not askContinue():
            break

    except ValueError:
        print('Invalid Age: Please enter a valid number for age')

print ("\n{}{:=^50}{}".format(Color.redBold,emojize("CHALLENGE 69 END" + Emoji.challenge),Color.reset))
