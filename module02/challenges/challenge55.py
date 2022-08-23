
from datetime import date
from multiprocessing.connection import wait
import this
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

print("{}Write a software that ask to the user the weight of 5 people and check the biggest one{}".format(colorDic['blueBold'],colorDic['end']))

fat = 0
thin = 0 
for i in range (1,6):
    weight = float(input('type here the weight pearson {}: '.format(i)))
    if i ==1:
        fat= weight
        thin= weight
    else:
        if weight > fat:
            fat = weight
        if weight < thin:
            thin = weight



print('The biggest weight is {}Kg'.format(fat))
print('The smallest weight is {}Kg'.format(thin))

print ("{}{:=^50}{}".format(colorDic['redBold'], emojize("CHALLENGE 52 END :crossed_swords:  "), colorDic['end']))