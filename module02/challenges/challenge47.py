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

print ("{}{:=^50}{}".format(colorDic['redBold'], emojize("CHALLENGE 47 :crossed_swords:  "), colorDic['end']))
print("{}Write a software that show all pairs numbers from 1 to 50{}".format(colorDic['yellowBold'],colorDic['end']))

for i in range (1,51):
    if i%2 == 0 :
        print( i,end=' ')

print("\n\n other way  to solve it:\n".upper())

for i in range (2,51, 2):
    print( i,end=' ')

print ("\n{}{:=^50}{}".format(colorDic['redBold'], emojize("CHALLENGE 47 END :crossed_swords:  "), colorDic['end']))