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

print ("{}{:=^50}{}".format(colorDic['redBold'], emojize("CHALLENGE 50 :crossed_swords:  "), colorDic['end']))

print("{}Write a software that ask to the user 6 numbers AND sum only the pairs {}".format(colorDic['blueBold'],colorDic['end']))

s=0

for i in range (1,7):
    number = int(input("Type here a number: ").strip())
    if number%2 == 0 :
        s +=number
print(s)
    

print ("{}{:=^50}{}".format(colorDic['redBold'], emojize("CHALLENGE 50 END :crossed_swords:  "), colorDic['end']))