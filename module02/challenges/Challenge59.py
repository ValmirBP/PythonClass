from emoji import emojize


class color:
    black = '\033[30m'
    red = '\033[31m'
    green = '\033[32m'
    orange = '\033[33m'
    blue = '\033[34m'
    purple = '\033[35m'
    cyan = '\033[36m'
    lightGrey = '\033[37m'
    darkGrey = '\033[90m'
    lightRed = '\033[91m'
    lightGreen = '\033[92m'
    yellow = '\033[93m'
    lightBlue = '\033[94m'
    pink = '\033[95m'
    lightCyan = '\033[96m'
    reset = '\033[0m'

print(color.green, "\n"," CHALLENGE 59 ".center(50, emojize(":axe:")),color.reset, "\n")

print(color.cyan,
"""Create a program that reads two values and displays a menu on the screen:
[ 1 ] add
[ 2 ] multiply
[ 3 ] greater
[ 4 ] new numbers
[ 5 ] exit the program

Your program should perform the requested operation in each case.
"""
, color.reset)

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
            return number1,number2
        except ValueError:
            print (color.red,"\n wrong input",color.reset)

def main():
    number1, number2= insert_numbers()
    while True:
        print("\n[ 1 ] Add")
        print("[ 2 ] Multiply")
        print("[ 3 ] Greater")
        print("[ 4 ] New numbers")
        print("[ 5 ] Exit the program")

        choice = int(input("Choose an option: "))

        if choice == 1:
            result = add(number1, number2)
            print("\n Result of addition:", result)
        elif choice == 2:
            result = multiply(number1, number2)
            print("\n Result of multiplication:", result)
        elif choice == 3:
            result = greater(number1, number2)
            print("\n Greater number:", result)
        elif choice == 4:
            number1, number2= insert_numbers()
        elif choice == 5:
            print("Exiting the program...")
            break
        else:
            print("Invalid option. Please choose again.")

main()

print(color.green, "\n"," CHALLENGE 59 END ".center(50, emojize(":axe:")),color.reset, "\n")