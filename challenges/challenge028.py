from random import randint
from emoji import emojize


print("{:=^50}\n".format(emojize(" CHALLENGE 028 :crossed_swords:  ")))
print ("Write  a software that the computer choose a number between 0 and 5 and check for the user guess it")

n1 = randint(0,5)
guess = int(input("Can you guess the  number between  0-5\n Type it here: "))

if n1 == guess:
    print("Yeah! you are right the number is {}" .format(n1))
else:
    print("Sorry! the number is {}, Try again later".format(n1))



print("{:=^50}\n".format(emojize(" CHALLENGE 028 END :2nd_place_medal:  ")))
