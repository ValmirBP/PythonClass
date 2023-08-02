from emoji import emojize
from ClassColorsEmojis import *

print ("{}{:=^50}{}".format(Color.greenBold, emojize("CHALLENGE 52" + Emoji.challenge), Color.reset))

print(f"""{Color.cyan}Write a software that ask to the user a number and show
the divisors between 1 and itself {Color.reset}""")

prime = int(input("Type here a number: "))

print(f"The number between 1 and {prime} are:")
tot = 0

for i in range (1, prime+1 ):
    if  prime % i == 0:
        print(f"{Color.blue} {i} {Color.reset}", end = " ")
        tot += 1
    else:
        print(f"{Color.green} {i} {Color.reset}", end=" ")

print (f"\n{Color.green}The number {prime} was divided {tot} times{Color.reset}")
if tot == 2:
    print(f'{Color.cyan}For this reason the number is PRIME{Color.reset}')
else:
    print(f'{Color.cyan}For this reason the number is NOT A PRIME{Color.reset}')


print ("\n{}{:=^50}{}".format(Color.greenBold, emojize("CHALLENGE 52 END" + Emoji.challenge), Color.reset))