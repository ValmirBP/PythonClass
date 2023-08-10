from ClassColorsEmojis import *
from emoji import emojize


print ("{}{:=^50}{}".format(Color.redBold,emojize("CHALLENGE 63 " + Emoji.challenge),Color.reset))
print(f"""\n{Color.cyan}Write a program that reads any integer number N and displays the first N
elements of a Fibonacci Sequence on the screen.
 {Color.reset}\n""")

firstTerm = 0
secondTerm = 1
count = 3

while True:
    try:
        numberOfImputs = int(input("Enter the Quantity of terms you want for Fibonacci Sequence  : "))
        break
    except ValueError:
        print(f"\n{Color.redBold}Invalid input.{Color.reset}")

print(f'{Color.green} {firstTerm} {Color.reset}',end='-')
print(f'{Color.green} {secondTerm} {Color.reset}',end='-')

while count <= numberOfImputs:
    thirdTerm = firstTerm + secondTerm
    print(f'{Color.green} {thirdTerm} {Color.reset}',end= '-')
    firstTerm = secondTerm
    secondTerm = thirdTerm
    count += 1

print(f'{Color.green} END {Color.reset}')


print ("\n{}{:=^50}{}".format(Color.redBold,emojize("CHALLENGE 63 END" + Emoji.challenge),Color.reset))