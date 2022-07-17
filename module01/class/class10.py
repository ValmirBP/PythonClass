from audioop import avg
from emoji import emojize


print("{:=^50}".format(emojize("CLASS 10 :snake: ")))
# print("{: ^50}".format("CONDITIONAL STRUCTURES "))

# print("{: ^50}".format("\nCAR AGE "))
# age = int(input("Type how much time you have both your car in years: ").strip())
# print("The age  of your car is {} year old \nSo is possible to conclude that you car is: ".format(age))

# if age <= 3:
#     print("New!")
# else:
#     print("OLD!")

# print("{: ^50}".format("SIMPLIFIED VERSION "))
# print("New!" if age <=3 else "OLD!")

# print("{: ^50}".format("\nDoes Your name have Valmir? "))

# name = input("Type your name full: ").strip().title()

# if name.startswith("Valmir"):
#     print("Wow your name is so bealtfull and powerfull")
#     print("Nice to meet you {}".format(name))
# else:
#     print("Nice to meet you {}".format(name))

print("{: ^50}".format("\nClass average "))

grade1 = float(input("Type the First grade: "))
grade2 = float(input("Type the Second grade: "))
# av = avg(grade1,grade2)
av = (grade1+grade2)/2

print ("Your average is {}".format(av))

if av >= 7.0:
    print("Congrats you average is alsome")
else:
    print("Congrats you average is not alsome, Plase focus  little  more")

print("{:=^50}\n".format(emojize("CLASS 10 END:snake: ")))
