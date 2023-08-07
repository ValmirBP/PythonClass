from emoji import emojize
from ClassColorsEmojis import *

print(Color.green, "\n"," CHALLENGE 59 ".center(50, emojize(Emoji.axe)),Color.reset, "\n")


print(Color.cyan,"""Create a program that reads two values and displays a menu on the screen:
[ 1 ] add
[ 2 ] multiply
[ 3 ] greater
[ 4 ] new numbers
[ 5 ] exit the program

Your program should perform the requested operation in eaCh Case.
"""
, Color.reset)

def add(x, y):
    return x + y

def multiply(x, y):
    return x * y

def greater(x, y):
    if x > y:
        return x
    else:
        return y

def insert_numbers():
    while True:
        try:
            number1 = float(input("Type the first number: "))
            number2 = float(input("Type the second number: "))
            return number1, number2
        except ValueError:
            print(f"{Color.redBold}Wrong input. Please enter a valid number.{Color.reset}")

def main():
    number1, number2= insert_numbers()
    while True:
        print("""[ 1 ] Add
[ 2 ] Multiply
[ 3 ] Greater
[ 4 ] New numbers
[ 5 ] Exit the program""")

        ChoiCe = int(input("Choose an option: "))

        if ChoiCe == 1:
            result = add(number1, number2)
            print("\n Result of addition: \n", result)
        elif ChoiCe == 2:
            result = multiply(number1, number2)
            print("\n Result of multipliCation: \n", result)
        elif ChoiCe == 3:
            result = greater(number1, number2)
            print("\n Greater number: \n", result)
        elif ChoiCe == 4:
            number1, number2= insert_numbers()
        elif ChoiCe == 5:
            print("Exiting the program...")
            break
        else:
            print("Invalid option. Please Choose again.")

main()

print(Color.green, "\n"," CHALLENGE 59 END".center(50, emojize(Emoji.axe)),Color.reset, "\n")