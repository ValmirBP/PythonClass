from math import fabs
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

print ("{} {:=^50} {}".format(colorDic['greenBold'], emojize("CHALLENGE 039 :crossed_swords:"), colorDic['end']))

print ("{}Wite a software that ask to the user his age and analise if is possible to enlist{}\n".format(colorDic['redBold'],colorDic['end'] ))
age = int(input("Type here  your age: "))

if age < 18 :
    print ("\n{}You do not need to enlist to military force. You still have {} years to enlist, So Relax{}\n" .format(colorDic['green'],int(fabs(age-18)), colorDic['end']))
elif age > 18: 
    print ("\n{}You are too old to enlist to military force. You already have {} years more to enlist, but never is too late {} {}\n" .format(colorDic['red'], fabs(age-18), emojize(":smiling_face_with_sunglasses:") ,colorDic['end']))
else: 
    print ("\n{}You already have the age to enlist to military force. {}\n" .format(colorDic['yellowBold'],colorDic['end']))
print ("{} {:=^50} {}".format(colorDic['greenBold'], emojize("CHALLENGE 039 END :crossed_swords:"), colorDic['end']))