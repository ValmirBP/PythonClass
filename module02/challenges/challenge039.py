from math import fabs
from emoji import emojize
from ClassColorsEmojis import *



print ("{} {:=^50} {}".format(Color.greenBold, emojize("CHALLENGE 039"+ Emoji.challenge), Color.reset))
print ("{}Wite a software that ask to the user his age and analyse if is possible to enlist{}\n"
       .format(Color.redBold,Color.reset ))

while True:
    try:
        age = int(input("Type here  your age: "))
        break
    except ValueError:
        print(Color.redBold,"Invalid input", Color.reset)

if age < 18 :
    print ("\n{}You do not need to enlist to military force. You still have {} years to enlist, So Relax{}\n"
           .format(Color.green,int(fabs(age-18)), Color.reset))
elif age > 18:
    print ("\n{}You are too old to enlist to military force. You already have {} years more to enroll, but never is too late {} {}\n"
           .format(Color.red, fabs(age-18), emojize(":smiling_face_with_sunglasses:") ,Color.reset))
else:
    print ("\n{}You already have the age to enroll to military force. {}\n" .format(Color.yellowBold,Color.reset))

print ("{} {:=^50} {}".format(Color.greenBold, emojize("CHALLENGE 039 END"+ Emoji.challenge), Color.reset))