from math import fabs
from emoji import emojize


print("{:=^50}\n".format(emojize(" CHALLENGE 035 :crossed_swords:  ")))

print("Write a software that ask to the user three measures of lines and check if is possible to become a triangle")

line1=float(input("Write a measure of line1: "))
line2=float(input("Write a measure of line2: "))
line3=float(input("Write a measure of line3: "))

if line1 > fabs(line2-line3) and (line2+line3) > line1 :
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

if r1=="true" and r2=="true" and r3=="true":
    print("It is a triangle")
else:
    print("It is " + "not ".upper() + "a triangle" )

print("{:=^50}".format(emojize(" CHALLENGE 035 :1st_place_medal:  ")))