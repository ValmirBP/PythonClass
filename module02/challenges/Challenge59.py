from unittest import result


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


print(color.green, "\n", " CHALLENGE 58 ".center(
    50, emojize(":axe:")), color.reset, "\n")

print(color.cyan, "Create a software that read 2 values and shows a menuÉ The software must do each operation selected in each case", color.reset)


def InputNums():
    try:
        number1 = int(input("Type here the first number"))
        number2 = int(input("Type here the Second number"))
    except ValueError:
        print("bad input")
    return number1, number2


def menu():
    print("What do you  want to do to  these numbers ?")
    try:
        sumNums = int(input("Sum [1]"))
        multiplyNums = int(input("multiplication [2]"))
        biggerNums = int(input("check the Bigger [3]"))
        newNums = int(input("New numbers [4]"))
        exitMenu = int(input("Exit [5]"))
    except ValueError:
        print("bad input")
    return sumNums, multiplyNums, biggerNums, newNums, exitMenu


def main():
    print(color.green, "\n", " CHALLENGE 59 ".center(
        50, emojize(":axe:")), color.reset, "\n")


print(color.green, "\n", " CHALLENGE 59 ".center(
    50, emojize(":axe:")), color.reset, "\n")
