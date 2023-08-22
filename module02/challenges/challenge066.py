from ClassColorsEmojis import *
from emoji import emojize


print ("{}{:=^50}{}".format(Color.redBold,emojize("CHALLENGE 66 " + Emoji.challenge),Color.reset))

print(f"""\n{Color.cyan} Create a program that reads integer numbers from the keyboard.
The program will only stop when the user enters the value 999, which is the stop condition.
In the end, display how many numbers were entered and what their sum was (excluding the flag).
{Color.reset}\n""")

count = 0
numSum = 0

while True:

    try:
        num = int(input(f'Enter a number: Enter [999] to exit  '))

        if num == 999:
            break

        else:
            count += 1
            numSum += num
    except ValueError:
        print(f'{Color.redBold} \nInvalid input,Try again\n {Color.reset}')

print(f"""{Color.cyan}\nNumbers entered: {count}
Sum between numbers: {numSum} {Color.reset}""")


print ("\n{}{:=^50}{}".format(Color.redBold,emojize("CHALLENGE 66 END" + Emoji.challenge),Color.reset))