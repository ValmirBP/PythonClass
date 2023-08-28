from ClassColorsEmojis import *
from emoji import emojize

print ("{}{:=^50}{}".format(Color.redBold,emojize("CHALLENGE 72 " + Emoji.challenge),Color.reset))

print(f"""\n{Color.cyan}Create a program that has a fully populated pair with a long count from zero
to twenty. Your program should read a number from the keyboard (between 0 and 20)
and display it in full.
{Color.reset}\n""")

numbers = ("zero","One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten",
    "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen",
    "Eighteen", "Nineteen", "Twenty")

while True:
    try:
        userChoice = int(input(f'{Color.greenBold}\nEnter  number  between 0 and 20: {Color.reset}'))
        if 0 <= userChoice <= 20:
                show = numbers[userChoice]
                print(f'{Color.blueBold}\nYour number is {show} {Color.reset}')
                break
        else:
                print(f' {Color.redBold}\nWrong input {userChoice} {Color.reset}')
    except ValueError:
        print(f'{Color.redBold}\nInvalid number {Color.reset}')
print ("\n{}{:=^50}{}".format(Color.redBold,emojize("CHALLENGE 72 END" + Emoji.challenge),Color.reset))
