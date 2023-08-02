
from datetime import date
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

print ("{}{:=^50}{}".format(colorDic['redBold'], emojize("CHALLENGE 52 :crossed_swords:  "), colorDic['end']))

print("{}Write a software that ask to the user the birthday of 7 people and  show how many rached 18 years or more {}".format(colorDic['blueBold'],colorDic['end']))

actualYear= date.today().year
majority = 0
minority = 0

for i in range (1,8):
    birthday =int(input('Type here the year of the birth: '))
    age = actualYear - birthday

    if age >= 21:
     majority += 1
    else:
       minority +=1

print ('{}In total {} people reached the majority and {} are minority {}'.format(colorDic['greenBold'], majority, minority, colorDic['end']))

print ("{}{:=^50}{}".format(colorDic['redBold'], emojize("CHALLENGE 52 END :crossed_swords:  "), colorDic['end']))