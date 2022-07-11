from turtle import speed
from emoji import emojize

print("{:=^50}\n".format(emojize(" CHALLENGE 028 :crossed_swords:  ")))
print ("Write a software that read the speed of a car imputed and check if it is over than 80km/h if is over wil be necessary to calculate the  value  of the tax consider U$7,00 for each kilometer over \n ")

speed = float(input("Type here the speed of the car: ").strip())

if speed > 80:
    tax = (speed - 80) * 7
    print("\nThe speed is over of the permitted in {}, so the tax you must to pay is U$ {:.2f}" .format(speed-80,tax))
else:
    print("\nPerfect your speed is {} \nYou are a very prudent driver keep on".format(speed))



print("{:=^50}\n".format(emojize(" CHALLENGE 028 END :2nd_place_medal:  ")))
