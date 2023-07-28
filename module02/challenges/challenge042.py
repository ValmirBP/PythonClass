from math import fabs
from emoji import emojize
from ClassColorsEmojis import *

print("{}{:=^50}{}".format(Color.green, emojize("CHALLENGE 42"+ Emoji.challenge), Color.reset))
print(f"""\n{Color.red}Write a software that ask to the user the  size of the three lines and check if,
is possible to create a triangle and say the type of triangle\n{Color.reset}\n""")

while True:
    try:
        line1 = float(input("Type the size of the line 1: ").strip())
        line2 = float(input("Type the size of the line 2: ").strip())
        line3 = float(input("Type the size of the line 3: ").strip())
        break
    except ValueError:
        print(f"{Color.redBold}\nInvalid input\n{Color.reset}")

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
    print(emojize(f"\n{Color.blueBold}It is a triangle :red_triangle_pointed_up:\n{Color.reset}"))

    if line1 == line2 == line3:
        print( emojize(f"{Color.blueBold}\nIt is an  equilateral triangle\n{Color.reset}"))

    elif line1 != line2 != line3:
        print( emojize(f"{Color.blueBold}\nIt is an  scalene triangle\n{Color.reset}"))

    elif line1 == line2 != line3:
        print( emojize(f"{Color.blueBold}\nIt is an  isosceles triangle\n{Color.reset}"))

    elif line2 == line1 != line3:
        print( emojize(f"{Color.blueBold}\nIt is an  isosceles triangle\n{Color.reset}"))

    elif line3 == line1 != line2:
        print( emojize(f"{Color.blueBold}\nIt is an  isosceles triangle\n{Color.reset}"))

    elif line3 == line2 != line1:
        print( emojize(f"{Color.blueBold}\nIt is an  isosceles triangle\n{Color.reset}"))

    elif line1 == line3 != line2:
        print( emojize(f"{Color.blueBold}\nIt is an  isosceles triangle\n{Color.reset}"))
else:
    print( emojize(f"{Color.redBold}\nIt is not a triangle\n{Color.reset}"))


print("{}{:=^50}{}".format(Color.green, emojize("CHALLENGE 42 END"+ Emoji.challenge), Color.reset))



# 123
# 132
# 213
# 231
# 312
# 321
