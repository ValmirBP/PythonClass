from ClassColorsEmojis import *
from emoji import emojize

print ("{}{:=^50}{}".format(Color.redBold,emojize("CHALLENGE 80 " + Emoji.challenge),Color.reset))

print(f"""\n{Color.cyan} Create a program that reads the name and two grades of several students
and stores everything in a composite list. At the end, show a report card containing each student's
average and allow the user to show each student's grades individually.
{Color.reset}\n""")

classStudents=[]
student=[]
grades = []

def checkEmptyName():
    while True:
        name = str(input(f'{Color.greenBold}Enter the name of the student:{Color.reset}'))
        if name == '' :
            print(f'{Color.red} Name can´t be empty{Color.reset}')
        else:
            return name

def checkGrade1(name):
    while True:
        try:
            grade1 = float(input(f'{Color.greenBold}Enter the first grade for student {name}: {Color.reset}'))
        except ValueError:
            print(f'{Color.red}Invalid grade 1 for {name}{Color.reset}')
        return grade1

def checkGrade2(name):
    while True:
        try:
            grade2 = float(input(f'{Color.greenBold}Enter the second grade for student {name}: {Color.reset}'))
        except ValueError:
            print(f'Invalid grade 2 for {name}')
        return grade2

def checkNum():
    while True:
        try:
            stdNum = int(input(f'{Color.greenBold}Enter the number of student: [999] to exit '))
        except ValueError:
            print(f'{Color.red}Invalid input{Color.reset}')
        return stdNum

def askContinue():
    while True:
        ask = input(f'{Color.greenBold}Do you want to continue? [Y]Yes [N]No {Color.reset}').strip().upper()
        if ask[0] == 'Y':
            return True
        if ask[0] == 'N':
            return False
        else:
            print(f'{Color.redBold}\nInvalid input, please enter Y or N{Color.reset}')

while True:
    name = checkEmptyName()
    grade1 = checkGrade1(name)
    grade2 = checkGrade2(name)
    avg = (grade1+grade2)/2
    student.append(name), grades.append(grade1), grades.append(grade2)
    student.append(grades[:]), student.append(avg), classStudents.append(student[:])
    grades.clear(), student.clear()
    ask =  askContinue()
    if not ask:
        break

print(classStudents)


print(f'{"No.":<4}{"NAME":<10}{"AVG":>8}')
for std,avg in enumerate(classStudents):
    print(f'{Color.greenBold}{std+1:<4}{classStudents[std][0]:<10}{classStudents[std][2]:>8}{Color.reset}')


while True:
    find = checkNum()-1
    if find <= len(classStudents)- 1:
        print(f'the  student {classStudents[find][0]} has the grades {classStudents[find][1]}')
    else:
        print('there is no student with this number on the list try again')
    ask = askContinue()
    if not ask:
        break

print ("\n{}{:=^50}{}".format(Color.redBold,emojize("CHALLENGE 80 END" + Emoji.challenge),Color.reset))
