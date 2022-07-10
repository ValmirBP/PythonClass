from emoji import emojize


print("{:=^50}".format(emojize("CLASS 10 :snake: ")))
print("{: ^50}".format("CONDITIONAL STRUCTURES "))

age = int(input("Type how much time you have both your car in years: ").strip())
print("The age  of your car is {} year old \nSo is possible to conclude that you car is: ".format(age))

if age <= 3:
    print("New!")
else:
    print("OLD!")

print("{: ^50}".format("SIMPLIFIED VERSION "))
print("New!" if age <=3 else "OLD!")

print("{:=^50}\n".format(emojize("CLASS 10 END:snake: ")))
