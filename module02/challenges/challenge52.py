from ast import If
from emoji import emoji_list, emojize


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

print("{}Write a software that ask to the user a number and show the divisors between 1 and itself {}".format(colorDic['blueBold'],colorDic['end']))

prime = int(input("Type here a number: "))

print("The number between 1 and {} are:".format(prime)) 

for i in range (1,(prime+1)):
    if 1%i == 0 and prime%i == 0:
        print(i)
    

print ("{}{:=^50}{}".format(colorDic['redBold'], emojize("CHALLENGE 52 END :crossed_swords:  "), colorDic['end']))