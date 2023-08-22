from ClassColorsEmojis import *
from emoji import emojize


print ("{}{:=^50}{}".format(Color.redBold,emojize("CHALLENGE 65 " + Emoji.challenge),Color.reset))

print(f"""\n{Color.cyan}Create a program that reads multiple integer numbers from the keyboard.
At the end of the execution, display the average of all values and which were the highest and
lowest values entered. The program should ask the user whether they want to continue entering
values or not{Color.reset}\n""")

answer = 'S'
inputsSum  = inputsSum = count= smallest = biggest = 0


while True:

    try:
        while answer == 'S':
            userInput = int(input("Enter the a number: "))
            inputsSum += userInput; count += 1

            if count <= 1 :
                smallest = biggest = userInput

            else:

                if userInput > biggest:
                    biggest = userInput

                if userInput < smallest:
                    smallest = userInput

            print(f'{Color.green}You typed: {userInput}\n{Color.reset}')
            answer = input(f'{Color.darkGrey}Do you want to continue? [S,N]\n{Color.reset}').upper().strip()

            if answer == 'N':
                print(f'{Color.greenBold} You typed {count} numbers \n{Color.reset}')
                print(f'{Color.greenBold} The sum average of these numbers is {inputsSum/count}\n {Color.reset}')
                print(f'{Color.greenBold} The biggest numbers is {biggest}\n {Color.reset}')
                print(f'{Color.greenBold} The smallest is {smallest}\n {Color.reset}')
                print(f'{Color.redBold} End! {Color.reset}')

            elif answer != 'S' or answer != 'N' :

                while answer != 'S':
                    print(f'{Color.redBold} \nInvalid input,Try again\n {Color.reset}')
                    answer = input(f'{Color.darkGrey}Do you want to continue? [S,N]\n {Color.reset}').upper().strip()

                    if answer == 'N':
                        print(f'{Color.greenBold} You typed {count} numbers \n{Color.reset}')
                        print(f'{Color.greenBold} The sum average of these numbers is {inputsSum/count}\n {Color.reset}')
                        print(f'{Color.greenBold} The biggest numbers is {biggest}\n {Color.reset}')
                        print(f'{Color.greenBold} The smallest is {smallest}\n {Color.reset}')
                        print(f'{Color.redBold} End! {Color.reset}')
        break

    except ValueError:

        print(f'{Color.redBold} \nInvalid input,Try again\n {Color.reset}')

print ("\n{}{:=^50}{}".format(Color.redBold,emojize("CHALLENGE 65 END" + Emoji.challenge),Color.reset))