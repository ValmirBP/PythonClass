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

print ("{}{:=^50}{}".format(colorDic['redBold'], emojize("CHALLENGE 49 :crossed_swords:  "), colorDic['end']))
print("{}Refactor the Challenge 09{}".format(colorDic['blueBold'],colorDic['end']))

table = int(input("Type here the  number  of the table that you want: ").strip())
for i in range (0,11):
    print ("{} x {} = {}{}{}". format(table, i,colorDic['green'], table*i, colorDic['end']))

print ("{}{:=^50}{}".format(colorDic['redBold'], emojize("CHALLENGE 49 END :crossed_swords:  "), colorDic['end']))