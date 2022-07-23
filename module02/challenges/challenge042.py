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

print("{}{:=^50}{}".format(colorDic['green'], emojize("CHALLENGE 42 :crossed_swords:"), colorDic['end']))
print("{}Write a software that ask to the user the  size of the three lines and check if it is possible to create a triangle and say the type of triangle{}".format(colorDic["red"], colorDic['end']))

line1 = float(input("Type the size of the line 1: ").strip())
line2 = float(input("Type the size of the line 2: ").strip())
line3 = float(input("Type the size of the line 3: ").strip())

if line1 > fabs(line2 - line3) and (line2 + line3) > line1 :
    r1="true"
else:
    r1="false"

if line2 > fabs(line1-line3) and (line1+line3) > line2:
    r2="true"
else:
    r2="false"

if line3 > fabs(line1-line2) and (line1+line2) > line3:
    r3="true"
else:
    r3="false"

if r1 == "true" and r2 == "true" and r3 == "true":
    print( emojize("{}It is a triangle :red_triangle_pointed_up:{}").format(colorDic["blueBold"], colorDic['end']))
    if line1 == line2 == line3:
        print( emojize("{}It is an  equilateral triangle{}").format(colorDic["blueBold"], colorDic['end']))

    elif line1 != line2 != line3:
        print( emojize("{}It is an  scalene triangle{}").format(colorDic["blueBold"], colorDic['end']))

    elif line1 == line2 != line3:
        print( emojize("{}It is an  isosceles triangle{}").format(colorDic["blueBold"], colorDic['end']))

    elif line2 == line1 != line3:
        print( emojize("{}It is an  isosceles triangle{}").format(colorDic["blueBold"], colorDic['end']))

    elif line3 == line1 != line2:
        print( emojize("{}It is an  isosceles triangle{}").format(colorDic["blueBold"], colorDic['end']))

    elif line3 == line2 != line1:
        print( emojize("{}It is an  isosceles triangle{}").format(colorDic["blueBold"], colorDic['end']))

    elif line1 == line3 != line2:
        print( emojize("{}It is an  isosceles triangle{}").format(colorDic["blueBold"], colorDic['end']))
else:
    print( emojize("{}It is not a triangle{}").format(colorDic["redBold"], colorDic['end']))


print("{}{:=^50}{}".format(colorDic['green'], emojize("CHALLENGE 42 END :crossed_swords:"), colorDic['end']))



# 123
# 132
# 213
# 231
# 312
# 321
