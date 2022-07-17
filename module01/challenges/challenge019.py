from emoji import emojize
from random import choice

print("{:=^50}\n".format(emojize(" CHALLENGE 019 :crossed_swords:  ")))

print(" Write a softare that read the name of 4 people and show on screen the The name in Random\n")

studant1 = str(input('Tipe the name of the fist studant ') )
studant2 = str(input('Tipe the name of the Second studant '))
studant3 = str(input('Tipe the name of the Third studant '))
studant4 = str(input('Tipe the name of the fourth studant '))
lst=[studant1,studant2,studant3,studant4]
chce=choice(lst)
print("\nThe chosen  studant was {}".format(chce))


print("{:=^50}".format(emojize(" CHALLENGE 019 :2nd_place_medal:  ")))