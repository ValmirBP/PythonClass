from emoji import emojize
from ClassColorsEmojis import *

print("{} {:=^50} {} ".format(Color.greenBold, emojize("CHALLENGE 037 :crossed_swords:"), Color.reset))

print("""Write a software that ask  for the user an  integer number  and  ask it which numeric base want
to convert the number\n""")
flag = True

while True:
    try:
        n1 = int(input("{}Type a number: {}".format(Color.green, Color.reset)))
        break
    except ValueError:
        print(Color.redBold, "Please enter  correct input and  try again", Color.reset)

while flag:
    convert = str(input(
        """ What base do you want to convert consider
        {}Binary (bin){}
        {}Octal (oc){}
        {}Hexadecimal (hex)):{} """.format(Color.blueBold, Color.reset,
                                       Color.greenBold, Color.reset,
                                       Color.yellowBold, Color.reset))).strip().lower()

    if convert == "bin":
        print(bin(n1))
        flag = False
    elif convert == "oc":
        print(oct(n1))
        flag = False
    elif convert == "hex":
        print(hex(n1))
        flag = False
    else:
        print("Invalid option")

print("{} {:=^50} {} ".format(Color.greenBold, emojize("CHALLENGE 037 END :crossed_swords:"), Color.reset))
