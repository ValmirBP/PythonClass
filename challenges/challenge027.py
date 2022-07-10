from emoji import emojize


print("{:=^50}\n".format(emojize(" CHALLENGE 027 :crossed_swords:   ")))

print("Write a software that read the full name  and show the frist and the last name Typed")

name = input("Type your full name: ").strip()
nameLst=name.split()

print("The Fist name is:  {}".format(nameLst[0]))
print("The Last name is:  {}".format(nameLst[len(nameLst)-1]))

print("{:=^50}\n".format(emojize(" CHALLENGE 027 :2nd_place_medal:  ")))
