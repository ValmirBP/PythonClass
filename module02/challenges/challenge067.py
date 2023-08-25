from ClassColorsEmojis import *
from emoji import emojize

print ("{}{:=^50}{}".format(Color.redBold,emojize("CHALLENGE 67 " + Emoji.challenge),Color.reset))

print(f"""\n{Color.cyan} Create a program that displays the multiplication table of various numbers,
one at a time, for each value entered by the user. The program will be interrupted
when a negative number is entered.
{Color.reset}\n""")

def multiplicationTable():

    while True:
        try:
                continueNumber =  int(input(f"""{Color.blueBold}Enter the multiplication table  you wanna see
    [any negative number] to exit: {Color.reset}"""))
                print("\n")

                if continueNumber < 0:
                 break

                for i in range (0,11):
                    print (f'{Color.blue} {continueNumber} x {i} = {Color.green} {continueNumber * i} {Color.reset}')

                print("\n")

        except ValueError:
            print (f'{Color.red}Invalid input {Color.reset}')

multiplicationTable()
print(f'{Color.greenBold}END{Color.reset}')

print ("\n{}{:=^50}{}".format(Color.redBold,emojize("CHALLENGE 67 END" + Emoji.challenge),Color.reset))