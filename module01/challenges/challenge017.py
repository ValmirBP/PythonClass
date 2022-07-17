from emoji import emojize
from math import hypot

print("{:=^50}\n".format(emojize(" CHALLENGE 017 :crossed_swords:  ")))
print("write a software that  calculates the Hypotenuse  and show the  value \n")

oppositeSide = float(input("Type the oposite side of  the Tringle "))
adjacentSide = float(input("Type the Adjacent side of the Tringle "))

print(" Opposite side Typed was {}\n Adjacent Side Typed is {}\n The result of the  Hypotenuse is {} ".format(oppositeSide,adjacentSide,hypot(oppositeSide,adjacentSide)))

print("{:=^50}".format(emojize("CHALLENGE 017 END :2nd_place_medal:  ")))