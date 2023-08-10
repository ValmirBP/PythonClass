from ClassColorsEmojis import *
from emoji import emojize


print ("{}{:=^50}{}".format(Color.redBold,emojize("CHALLENGE 60 " + Emoji.challenge),Color.reset))
print(f"""{Color.cyan}Create a program that reads any number and displays
it's factorial.{Color.reset}""")

while True:
    try:
        number = int(input("Enter the number for the factorial: "))

        if number == 0:
            print(f"\n{Color.green}The factorial of 0 is 1{Color.green}\n")
            break

        elif number < 0:
            print(f"""\n{Color.redBold}It is not possible to calculate the
factorial of a negative number.{Color.reset}\n""")
            print(f"\n{Color.cyan}Please try again.{Color.reset}\n")

        else:
            factorial = 1
            print(f"\n{Color.blue}Calculating {number}! \n{Color.reset}",end='')

            for i in range(1, number + 1):
                factorial *= i
                print(f"{Color.green} {i} ",end='')
                print("x" if i < number else '='  ,end='')
            print(f" {factorial} {Color.reset}")
            print(f"{Color.green}So the result for factorial of {number}! is {factorial}{Color.reset}")
            break

    except ValueError:
        print(f"\n{Color.redBold}Invalid input. Please enter a valid integer.\n{Color.reset}")

print ("{}{:=^50}{}".format(Color.redBold,emojize("CHALLENGE 60 END" + Emoji.challenge),Color.reset))