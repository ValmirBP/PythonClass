from cgi import test
from emoji import emojize
from datetime import date


print("{:=^50}\n".format(emojize(" CHALLENGE 032 :crossed_swords:  ")))

print("Write a software that read the actual year an check if it is leap year\n")

actualYear = int(input("type here the year tha you want to analyze or type 0 to analyze the actual year: "))

if actualYear == 0:
    actualYear = date.today().year

test1 = actualYear % 4
test2 = actualYear % 100
test3 = actualYear % 400

if test1 == 0 and test2 !=0  or test3 == 0:
    print(" {} Is Leap Year".format(actualYear))
else:
    print("{} is not Leap Year".format(actualYear))


print("{:=^50}\n".format(emojize(" CHALLENGE 032 END :2nd_place_medal:  ")))
