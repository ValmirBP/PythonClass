from random import randint
from emoji import emojize


print("{:=^50}\n".format(emojize(" CHALLENGE 033 :crossed_swords:  ")))

print("Write a Software that ask for the user 3 number and show the biggest ")

# n1 = int(input("Type the first number: "))
# n2 = int(input("Type the second number: "))
# n3 = int(input("Type the Third number: "))

n1 = randint(1,10)
n2 = randint(1,10)
n3 = randint(1,10)

print(n1, n2 , n3)

if n1 > n2 and n1 > n3 :
    print("Biggest {}".format(n1))

elif n2 > n1 and n2 > n3:
    print("Biggest {}".format(n2))

elif n3 > n1 and n3 > n2:
    print("Biggest {}".format(n3))

if n1 < n2 and n1 < n3:
    print("Smallest {}".format(n1))

elif n2 < n1 and n2 < n3:
    print("Smallest {}".format(n2))

elif n3 < n1 and n3 < n2:
    print("Smallest {}".format(n3))

print("{:=^50}\n".format(emojize(" CHALLENGE 033 END :2nd_place_medal:  ")))
