from ClassColorsEmojis import *
from emoji import emojize


print ("{}{:=^50}{}".format(Color.redBold,emojize("CHALLENGE 64 " + Emoji.challenge),Color.reset))

print(f"""\n{Color.cyan}Create a program that reads several integer numbers from the keyboard.
The program will only stop when the user enters the value 999, which is the stopping condition.
In the end, show how many numbers were entered and what was their sum
(excluding the flag).{Color.reset}\n""")

userInput = 0
inputsSum = 0
count = 0
while True:

    try:

        while userInput != 999:
            userInput = int(input("Enter the a number: "))
            inputsSum += userInput; count += 1
            print(f'{Color.green}You typed: {userInput}\n{Color.reset}')
            print (f'{Color.darkGrey}If you want to stop just press 999\n {Color.reset}')

            if userInput == 999:
                count -= 1; inputsSum -= 999
                print(f'{Color.greenBold} You typed {count} numbers \n{Color.reset}')
                print(f'{Color.greenBold} The sum between these numbers is {inputsSum}\n {Color.reset}')
                print(f'{Color.redBold} End! {Color.reset}')
        break

    except ValueError:

        print(f'{Color.redBold} \nInvalid input,Try again\n {Color.reset}')

print ("\n{}{:=^50}{}".format(Color.redBold,emojize("CHALLENGE 64 END" + Emoji.challenge),Color.reset))