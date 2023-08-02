from emoji import emojize
from ClassColorsEmojis import *

print ("{}{:=^50}{}".format(Color.greenBold, emojize("CHALLENGE 44 "+ Emoji.challenge), Color.reset))

print (Color.lightBlue,"""write software that calculate a value of a product considering its normal price and payment condition:
full: money|check 10%
full discount ticket 5%
part payment 3 times or more on credit card 20%""",Color.reset)

while True:
    try:
        total = float(input(f"{Color.blue}\nType  here  the total: {Color.reset}").strip())
        payMethod = int(input(f"""{Color.redBold}Now choose the payment
        [1]: money | check,
        [2]: Discount Ticket,
        [3]: Credit Card: {Color.reset}""").strip().upper())

        if payMethod == 1:
            total = total - (10/100 * total)
            print(f"\nthe total is: {Color.greenBold} ${total:.2f} {Color.reset}")
            break

        elif payMethod == 2:
            total = total - (5/100 * total)
            print(f"\nthe total is: {Color.greenBold} ${total:.2f} {Color.reset}")
            break

        elif payMethod == 3:
            total = total - (20/100 * total)
            print(f"\nthe total is: {Color.greenBold} ${total:.2f} {Color.reset}")
            break

        else:
            print (f"{Color.redBold}\ninvalid condition{Color.reset}")

    except ValueError:
            print (f"{Color.redBold}\ninvalid input{Color.reset}")

print ("{}{:=^50}{}".format(Color.greenBold, emojize("CHALLENGE 44 END"+ Emoji.challenge), Color.reset))
