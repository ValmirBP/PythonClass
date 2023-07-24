from emoji import emojize
from ClassColorsEmojis import *

print("{} {:=^50} {}".format(Color.greenBold, emojize(" CHALLENGE 036" + Emoji.challenge), Color.reset))

print("""Write a Software that asks the user for their wage, the value of a house, and the payment schedule.
Calculate the value of the monthly payment that does not exceed 30 percent of their wage, as
it is forbidden to exceed that amount.\n""")

while  True:
    try:
        wage = float(input("Type the wage: "))
        valueHouse = float(input("Type the value of the house: "))
        period = int(input("Type the period of payment in months: "))
        break
    except ValueError:
        print("the input is not  correct please try again\n")

percentageWage = (valueHouse / period) * 100 / wage
idealValue = (valueHouse * 100) / (wage * 30)


if percentageWage > 30:
    print("\nSorry! Unfortunately, it is not possible to approve your finance because it exceeds 30% of your wage.\n")
    print("""But it is possible to help you buy your house if you invest {:.2f}. It will be possible to
    approve\nand get {} months to pay\nor {} years.""".format(idealValue, (valueHouse / idealValue), (valueHouse / idealValue) / 12))

    answer = input("Do you want to accept the deal? (y/n) ")

    if answer.lower() == "y":
        print("\nGood! Contact any consultant to sign the proposal.")
    else:
        print("\nOk! See you next time.")

else:
    print("\nGood! Contact any consultant to sign the proposal.\n")

print("{} {:=^50} {}".format(Color.greenBold, emojize("CHALLENGE 036 END " + Emoji.challenge), Color.reset))
