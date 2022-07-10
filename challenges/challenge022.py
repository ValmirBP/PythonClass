from itertools import count
from emoji import emojize

print("{:=^50}\n".format(emojize(" CHALLENGE 022 :crossed_swords: ")))
print("Wrie a software hat recieve  from de  user  de  full name  asnd  show  on screen \nThe name in upper case \nThe name in lower case \nnumber of characters unconsidering the blancs \nnumber of chracters in first name \n")

name = input(emojize("Tipe here your name :red_question_mark: ")).strip()

print("Your name in  Upeer case:  {}".format(name.upper()))
print("Your name in  Lower case:  {}".format(name.lower()))
print("Your name have {} Characters".format(len(name)-name.count(" ")))
print("Your first name have {} Characters".format(len(name.split()[0])))


print("{:=^50}".format(emojize(" CHALLENGE 022 END :2nd_place_medal:")))