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

print ("{}{:=^50}{}".format(colorDic['redBold'], emojize("CHALLENGE 48 :crossed_swords:  "), colorDic['end']))
print("{}Write a software that show all odd numbers from 1 to 500 and sum the multiplicators of 3 number{}".format(colorDic['blueBold'],colorDic['end']))

s=0
for i in range (1,500):
    if i%2 !=0 and i%3 == 0:
        s +=i 
print (s)

print ("{}{:=^50}{}".format(colorDic['redBold'], emojize("CHALLENGE 48 END :crossed_swords:  "), colorDic['end']))