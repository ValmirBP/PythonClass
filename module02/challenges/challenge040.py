
from statistics import mean

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

print("{} {:=^50} {}".format(colorDic['greenBold'], emojize("CHALLEGE 040 :crossed_swords:"), colorDic['end']))

print("{}Write a software that ask two grades from a classmate and analyses if he is approved or not consider 7.0 to be approved consider 1.0 to 10.0{}\n".format(colorDic['red'],colorDic['end']))

grade1 = float(input("Type here the First grade: ").strip())
grade2 = float(input("Type here the Second grade: ").strip())

gradeLst = [grade1,grade2]
res = mean(gradeLst)

if res >= 7.0:
    print("{}CONGRATULATIONS!!! You´re approved the average is {:.2f} {}\n".format(colorDic['greenBold'], res, colorDic['end']))

elif res < 5.0:
    print("{}SORRY! You are not approved the average is {:.2f} {}\n".format(colorDic['redBold'], res, colorDic['end']))

elif res > 5.0 and res < 6.9 :
    print("{}WOW! You are almost there, you do not reached enough points {:.2f} {}\n".format(colorDic['yellowBold'], res, colorDic['end']))
else: 
    print("invalid grades")
print("{} {:=^50} {}".format(colorDic['greenBold'], emojize("CHALLEGE 040 END :crossed_swords:"), colorDic['end']))
