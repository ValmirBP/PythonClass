from emoji import emojize
from math import radians, sin,cos,tan 

print("{:=^50}\n".format(emojize(" CHALLENGE 018 :crossed_swords:  ")))

print(" Write a softare that read an any angle and show the Tangent, cosine and sine of it\n")

angle=float(input("Tipe an angle "))
sinRes= sin(radians(angle))
cosnRes=cos(radians(angle))
tanRes=tan(radians(angle))

print("The sine is {:.3f} \nThe Cosine is {:.3f} \nand the Tangent is {:.3f} \nof the angle {}".format(sinRes,cosnRes,tanRes,angle))

print("{:=^50}".format(emojize(" CHALLENGE 018 :2nd_place_medal:  ")))