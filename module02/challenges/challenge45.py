from secrets import choice
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

print("{}{:=^100}{}".format(colorDic['greenBold'], emojize("CHALLENGE 45 :crossed_swords:"), colorDic['end']))
print("{}write a software that play{}" "{} Jokeeeeee  npooow....{}".upper().format(colorDic['blueBold'], colorDic['end'], colorDic['redBold'], colorDic['end']))
x= 1
sleep(1)
print(x)

x= x+1
sleep(1)
print(x)

x= x+1
sleep(1)
print(x)
print("GOO!\n")

jkpLst= ["1", "2" , "3"]
pc= int(choice(jkpLst))

player= int(input("choose \n[1]rock \n[2]Paper \n[3]Scissors: \n"))

if player == pc:
    print(pc, "\n")
    print("{}again{}".upper().format(colorDic['blueBold'], colorDic['end']))

elif player > pc:
    print(pc, "\n")
    print("{}You win!!!{}".upper().format(colorDic['greenBold'], colorDic['end']))

elif player < pc:
    print(pc, "\n")
    print("{}You loose!!!{}".upper().format(colorDic['redBold'], colorDic['end']))



print("{}{:=^100}{}".format(colorDic['greenBold'], emojize("CHALLENGE 45 END :crossed_swords:"), colorDic['end']))