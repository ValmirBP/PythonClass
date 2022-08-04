from multiprocessing.connection import wait
from time import sleep
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

print("{}{:=^50}{}".format(colorDic['redBold'], emojize("CHALLENGE 46 :crossed_swords:  "), colorDic['end']))
print("{}Write a software the shows a countdown for a fireshow for the end of the year{}".format(colorDic['blueBold'], colorDic['end']))

for i in range (10,-1,-1):
    print(i)
    sleep(1)
print(" \nhappy new year!!!".upper() + emojize(":fireworks:"*10))
print("{}{:=^50}{}".format(colorDic['redBold'], emojize("CHALLENGE 46 END :crossed_swords:  "), colorDic['end']))