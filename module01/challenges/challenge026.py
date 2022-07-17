from emoji import emojize

print("{:=^50}\n".format(emojize(" CHALLENGE 026 :crossed_swords:")))

print ("write a software that read from input and show how much the letter A is present show the 1st position and the last'\n")

typed = input ("type  something: ").lower().strip()

print("The word that you typed have {} characters".format(typed.count("a")))
print("The word that you typed there is a leter 'a' on {} position".format(typed.find("a")+1))
print("The word that you typed there is the letter 'a' at last {} position  ".format(typed.rfind("a")+1))

print("\n{:=^50}".format(emojize(" CHALLENGE 026 :2nd_place_medal:")))