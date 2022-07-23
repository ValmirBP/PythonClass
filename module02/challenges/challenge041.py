from datetime import date
from tkinter.messagebox import YES
from emoji import emojize




colorDic = {
    'bold'          : '\033[1m'
    ,'red'          : '\033[31m'
    ,'green'        : '\033[32m'
    ,'yellow'       : '\033[33m'
    ,'blue'         : '\033[34m'
    ,'redBold'      : '\033[1;31m'
    ,'greenBold'    : '\033[1;32m'
    ,'yellowBold'   : '\033[1;33m'
    ,'blueBold'     : '\033[1;34m'
    ,'end'          : '\033[m'
}

print("{}{:=^50}{}".format(colorDic['greenBold'], emojize("CHALLENGE 041 :crossed_swords:"), colorDic['end']))

print("{}Write a software that ask to the user the year of his birth and analyse the categories of a swimming competition{}\n".format(colorDic['red'], colorDic['end']))

birthYear = int(input("Type here your birth year: ").strip())

actualYear= date.today().year
age = actualYear - birthYear

if age == 9:
    stage = "Little"
    print("{}You are in category {} {}\n".format(colorDic['green'], stage, colorDic['end']))

elif age > 9 and age <= 14:
    stage = "childish"
    print("{}You are in category {} {}\n".format(colorDic['blue'], stage, colorDic['end']))

elif age > 14 and age <= 19:
    stage = "Junior"
    print("{}You are in category {} {}\n".format(colorDic['yellow'], stage, colorDic['end']))

elif age > 19 and age <= 20:
    stage = "Senior"
    print("{}You are in category {} {}\n".format(colorDic['blueBold'], stage, colorDic['end']))

elif age > 20:
    stage = "Master"
    print("{}You are in category {} {}\n".format(colorDic['yellowBold'], stage, colorDic['end']))

else:
    print("{}Sorry You are too young{}".format(colorDic['redBold'], colorDic['end']))


print("{}{:=^50}{}".format(colorDic['greenBold'], emojize("CHALLENGE 041 END :crossed_swords:"), colorDic['end']))