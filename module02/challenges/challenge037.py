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

print ("{} {:=^50} {} ".format(colorDic['greenBold'],emojize (" CHALLENGE 037 :crossed_swords:  "),colorDic['end']))

print("Write a software that ask  for the user an  integer number  and  ask it wich numeric base want  to convert the number\n")
n1 = int(input("{}Type a number: {}".format(colorDic['green'],colorDic['end'])))

convert = str(input("What basis do  you wnat  to convert  consider  \n{}Binary (bin){} \n{}Octal (oc){} \n{}Hexadecimal (hex):{}\n ".format(colorDic['blueBold'],colorDic['end'],colorDic['greenBold'],colorDic['end'],colorDic['yellowBold'], colorDic['end']))).strip().lower()

if convert == "bin":
    n1 = bin(n1)
    print(n1)
elif convert == "oc":
    n1 = oct(n1)
    print(n1)
elif convert == "hex":
    n1 = hex(n1)
    print(n1)
else:
    print("Invalid option")
    
print ("{} {:=^50} {} ".format(colorDic['greenBold'],emojize (" CHALLENGE 037 END :crossed_swords:  "),colorDic['end']))