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

print ("{}{:=^50}{}".format(colorDic['redBold'], emojize("CHALLENGE 51 :crossed_swords:  "), colorDic['end']))

print("{}Write a software that ask to the user the  fist number and the common differential number of a arithmetic progression of 10 positions {}".format(colorDic['blueBold'],colorDic['end']))

n1 = int(input("type here the 1st number of the AP: "))    
dif = int(input("Type here the differential number of the AP: "))


print("The AP between {} and {} in range of 10 is".format(n1, dif))
for  i in range (1,11):
    op = n1 + (i-1) * dif
    print(op, end=" ")

print ("\n{}{:=^50}{}".format(colorDic['redBold'], emojize("CHALLENGE 51 END :crossed_swords:  "), colorDic['end']))