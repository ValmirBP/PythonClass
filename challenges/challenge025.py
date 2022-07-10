from emoji import emojize

print("{:=^50}\n".format(emojize(" CHALLENGE 025 :crossed_swords:")))

print ("write a software that read from input the name and chek if there is 'Silva'\n")

name = input('Tipe your full name: ')
name = name.strip()
name = name.title()
print("Does your name have Silva ? {}".format("Silva" in name))


print("{:=^50}".format(emojize(" CHALLENGE 025 :2nd_place_medal:")))