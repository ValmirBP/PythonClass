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

print ("{}{:=^50}{}".format(colorDic['greenBold'], emojize(" CLASS 13 :snake: "), colorDic['end']))

print("{:=^50}".format("LOOP for"))

for i in range(10, -1, -1):
    print(i)
print("="* 50)

for i  in  range (0, 10, 2):
    print(i)

print ("{}{:=^50}{}".format(colorDic['greenBold'], emojize(" CLASS 13 END :snake: "), colorDic['end']))