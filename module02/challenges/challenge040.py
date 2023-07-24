
from statistics import mean
from emoji import emojize
from ClassColorsEmojis import *



print("{} {:=^50} {}".format(Color.greenBold, emojize("CHALLENGE 040", Emoji.challenge), Color.reset))

print("""{}Write a software that ask two grades from a classmate and analyses if he is approved or not consider
7.0 to be approved consider 1.0 to 10.0{}\n""" .format(Color.red,Color.reset))

while True:
    try:
        grade1 = float(input("Type here the First grade: ").strip())
        grade2 = float(input("Type here the Second grade: ").strip())
        break
    except ValueError:
        print (Color.red, "Invalid input", Color.reset)

gradeLst = [grade1,grade2]
res = mean(gradeLst)

if res >= 7.0:
    print("{}\nCONGRATULATIONS!!! You´re approved the average is {:.2f} {}\n".format(Color.greenBold, res, Color.reset))

elif res < 5.0:
    print("{}\nSORRY! You are not approved the average is {:.2f} {}\n".format(Color.redBold, res, Color.reset
))

elif res > 5.0 and res < 6.9 :
    print("{}\nWOW! You are almost there, you do not reached enough points {:.2f} {}\n"
          .format(Color.yellowBold, res, Color.reset))
else:
    print("invalid grades")
print("{} {:=^50} {}".format(Color.greenBold, emojize("CHALLENGE 040 END", Emoji.challenge), Color.reset))
