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
tot = 0

for i in range (1, prime+1 ):
    if  prime % i == 0:
        print("{}".format(colorDic['blue']) , i, "{}".format( colorDic['end']), end=" ")
        tot += 1
    else:
        print("{}".format(colorDic['green']) , i, "{}".format( colorDic['end']), end=" ")
    
print ("\n{}The number {} was divided {} times{}".format(colorDic['green'], prime, tot, colorDic['end']))
if tot == 2:
    print('For this reason the number is PRIME')
else:
    print('For this reason the number is NOT A PRIME')

    
print ("\n{}{:=^50}{}".format(colorDic['redBold'], emojize("CHALLENGE 52 END :crossed_swords:  "), colorDic['end']))