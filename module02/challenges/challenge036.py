from emoji import emojize
from ClassColorsEmojis import *

print("{} {:=^50} {}".format(Color.greenBold, emojize(" CHALLENGE 036" + Emoji.challenge), Color.reset))

print(Color.cyan,"""Write a Software that asks the user for their wage, the value of a house,
and the payment schedule. Calculate the value of the monthly payment that does not exceed 30 percent
of their wage, as it is forbidden to exceed that amount.\n""",Color.reset)

while  True:
    try:
        wage = float(input("Type the wage: "))
        valueHouse = float(input("Type the value of the house: "))
        period = int(input("Type the period of payment in months: "))
        break
    except ValueError:
        print(Color.redBold,"the input is not  correct please try again\n",Color.reset)

percentageWage = (valueHouse / period) * 100 / wage
idealValue = (valueHouse * 100) / (wage * 30)
yearsConv = (valueHouse / idealValue) / 12


if percentageWage > 30:

    print(Color.red,"""\nSorry! Unfortunately, it is not possible to approve your finance because it
exceeds 30% of your wage.\n""",Color.reset)

    print(f"""{Color.red}But it is possible to help you buy your house if you invest Ca${idealValue:.2f}.
It will be possible to approve and get {(valueHouse / idealValue)} months to pay or {yearsConv:.2f} years
to finish the purchase.{Color.reset}\n""")

    while True:
        answer = input("Do you want to accept the deal? (y/n) ").strip().lower()
        if answer.lower() == "y":
            print(Color.green,"\nGood! Contact any consultant to sign the proposal.",Color.reset)
        elif answer.lower() == "n":
            print(Color.green,"\nOk! See you next time.",Color.reset)
            break
        else:
            print(Color.redBold,"the input is not  correct please try again\n",Color.reset)
else:
    print(Color.green,"\nOk! See you next time.",Color.reset)

print("{} {:=^50} {}".format(Color.greenBold, emojize("CHALLENGE 036 END " + Emoji.challenge), Color.reset))
