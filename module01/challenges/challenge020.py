from emoji import emojize
from random import shuffle

print("{:=^50}\n".format(emojize(" CHALLENGE 020 :crossed_swords:  ")))

print(" Write a softare that read 4 names an show it in a random sequence\n")

studant1 = str(input('Tipe the name of the fist Studant '))
studant2 = str(input('Tipe the name of the second Studant '))
studant3 = str(input('Tipe the name of the third Studant '))
studant4 = str(input('Tipe the name of the fourth Studant '))
lst=[studant1,studant2,studant3,studant4]
ch=shuffle(lst)
print("\nThe order  is")
print(lst)

print("{:=^50}".format(emojize(" CHALLENGE 020 :2nd_place_medal:  ")))