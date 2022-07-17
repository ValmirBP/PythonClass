from itertools import count
from re import T
from emoji import emojize


from emoji import emojize

print("{:=^50}\n".format(emojize("CHALLENGE 023 :crossed_swords:  ")))
print("write a software that read  a numer  from  0  to 9999 and show on screen de separeted digits\n")

n1=input("Write a number with white sapces between them 'EX 1 2 3' : ")

print("the number is {}".format(n1.replace(" ","")))
print("the unit is {}".format(n1.split()[3]))
print("The teen is {}".format(n1.split()[2]))
print("The hundred is {}".format(n1.split()[1]))
print ("the thousand is {}".format(n1.split()[0]))

print ("\nOTHER WAY TO SOLVE IT \n")
n2 = int(n1.replace(" ",""))
u = n2 // 1 % 10
t = n2 // 10 % 10
h = n2 // 100 % 10
th = n2 // 1000 % 10

print("the number is {}".format(n1.replace(" ","")))
print("the unit is {}".format(u))
print("The teen is {}".format(t))
print("The hundred is {}".format(h))
print ("The thousand is {}".format(th))

print("{:=^50}\n".format(emojize("CHALLENGE 023 :2nd_place_medal:  ")))