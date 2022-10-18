from emoji import emojize


colorDic = {
    'bold'          : '\033[1m'
    ,'redBold'          : '\033[31m'
    ,'green'        : '\033[32m'
    ,'yellow'       : '\033[33m'
    ,'blue'         : '\033[34m'
    ,'redBold'      : '\033[1;31m'
    ,'greenBold'    : '\033[1;32m'
    ,'yellowBold'   : '\033[1;33m'
    ,'blueBold'     : '\033[1;34m'
    ,'end'          : '\033[m'
}

print ("{:=^50}".format(emojize("CHALLENGE 043 :crossed_swords:")))

print("{}Write a software that ask  for  the user his tall and  his weight and  calculate the  IMC{}".format(colorDic['blue'] , colorDic['end'] ))

print("{}following the instructions less than 18,5 thinness from 18,5 to 24,9 normal from 25 to 29,9 overweight from 30 to 34,9 obesity first grade from 35 to 39,9 obesity second garde bigger than 40 obesity third grade{}".format(colorDic['blue'] , colorDic['end']))

weight = float(input("Type here the  weight: ").strip())
tall = float(input("Type here the Tall: ").strip())
imc = weight / (tall * tall)

print("Your IMC is {:.2f}".format(imc))

if imc < 18.5:
    print("Thinness".upper().format(colorDic['yellowBold'], colorDic['end']))

elif imc > 18.5 and imc <= 24.9:
    print("Normal".upper().format(colorDic['greenBold'], colorDic['end']))

elif imc > 25 and imc <= 29.9:
    print("{}overweight{}".upper().format(colorDic['redBold'], colorDic['end']))

elif imc > 30 and imc <= 34.9:
    print("{}obesity first grade{}".upper().format(colorDic['redBold'], colorDic['end']))

elif imc > 35 and imc <= 39.9:
    print("{}obesity second grade{}".upper().format(colorDic['redBold'], colorDic['end']))

elif imc > 40:
    print("{}obesity second grade{}".upper().format(colorDic['redBold'], colorDic['end']))

print ("{:=^50}".format(emojize("CHALLENGE 043 END :crossed_swords:"))) 