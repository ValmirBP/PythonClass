from random import randint
from emoji import emojize


print("{:=^50}\n".format(emojize(" CHALLENGE 030 :crossed_swords:  ")))
print ("Write an software that ask for the user if a number and check if it is a pair or odd number\n")

n1 = int(input("Type a number here: ").strip())

pair = n1%2
if pair == 0:
    print("OK, the Typed number is {}, so it is Pair" .format(n1))
else:
    print("Sorry! the number is {}, so it is Odd".format(n1))

print("{:=^50}\n".format(emojize(" CHALLENGE 030 END :2nd_place_medal:  ")))
