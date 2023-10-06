from ClassColorsEmojis import *
from emoji import emojize

print ("{}{:=^50}{}".format(Color.redBold,emojize("CHALLENGE 90 " + Emoji.challenge),Color.reset))

print(f"""\n{Color.cyan} Create a program that reads the name and two grades of several students
and stores everything in a composite list. At the end, show a report card containing each
student's average and allow the user to show each student's grades individually.
{Color.reset}\n""")

student = dict()

def checkGrade ():
    while True:
        try:
            stdGrade = float(input(f'{Color.green} Enter the average of the student: {Color.reset}'))
            return  stdGrade
        except ValueError :
            print (f'{Color.redBold} invalid imput {Color.reset}')

stdName = str(input(f'{Color.greenBold} Enter the name of the  student: {Color.reset}'))
stdGrade = checkGrade()
student ['name'] = stdName
student ['avg '] = stdGrade

if student["avg "] >=7:
    student['status'] = 'Approved'

if student["avg "] <7:
    student['status'] = 'mockup course'

else:
    student['status'] = 'reproved'



for k,v in student.items():
    print(f'{Color.greenBold}The student {k} has the {k} {v}')
print ("\n{}{:=^50}{}".format(Color.redBold,emojize("CHALLENGE 90 END" + Emoji.challenge),Color.reset))
