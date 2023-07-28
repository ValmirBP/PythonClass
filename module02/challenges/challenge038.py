from ClassColorsEmojis import*
from emoji import emojize


print("{} {:=^50} {}".format(Color.greenBold, emojize("CHALLENGE 038"+ Emoji.challenge), Color.reset))

print("{}Write a software that ask  to the user two numbers integer and compare them{}\n".format(Color.redBold,Color.reset))
while True:
    try:
        n1 = int(input("\nType the first number: ").strip())
        n2 = int(input("\nType the second number: ").strip())
        break
    except ValueError:
        print(Color.redBold, "\ninvalid input", Color.reset)

if n1 > n2:
    print("\nThe number {}{}{} is bigger than  {}{}{}".format(Color.blue, n1, Color.reset, Color.yellow, n2, Color.reset))
elif n2 > n1:
    print("\nThe number {}{}{} is bigger than  {}{}{}".format(Color.blue, n2, Color.reset, Color.yellow, n1, Color.reset))
else:
    print("\nThere is no bigger or both are  equals")

print("{} {:=^50} {}".format(Color.greenBold, emojize("CHALLENGE 038 END"  + Emoji.challenge), Color.reset))