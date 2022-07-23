from turtle import color
from emoji import emojize


colorDic ={ 
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

print("{} {:=^50} {}".format(colorDic['greenBold'], emojize("CHALLENGE 038 :crossed_swords:"), colorDic['end']))

print("{}Write a software that ask  to the user two numbers integer and compare them{}\n".format(colorDic['redBold'],colorDic['end']))
n1 = int(input("Type the first number: ").strip())
n2 = int(input("Type the second number: ").strip())

if n1 > n2:
    print("\nThe number {}{}{} is bigger than  {}{}{}".format(colorDic['blue'], n1, colorDic['end'], colorDic['yellow'], n2, colorDic['end']))
elif n2 > n1:
    print("\nThe number {}{}{} is bigger than  {}{}{}".format(colorDic['blue'], n2, colorDic['end'], colorDic['yellow'], n1, colorDic['end']))
else:
    print("\nThere is no bigger or both are  equals")

print("{} {:=^50} {}".format(colorDic['greenBold'], emojize("CHALLENGE 038 END:crossed_swords:"), colorDic['end']))