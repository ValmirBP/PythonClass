from emoji import emojize
from ClassColorsEmojis import *


print ("{}{:=^50}{}".format(Color.redBold, emojize("CHALLENGE 49" + Emoji.challenge), Color.reset))
print(f"{Color.blueBold}Refactor the Challenge 09{Color.reset}")

while True:
        try:
            table = int(input("Enter the number of the  multiplication table that you want:").strip())
            break
        except ValueError:
             print (f'{Color.redBold}Invalid input{Color.reset}')

for i in range (0,11):
    print (f"{Color.yellowBold} {table} x {i} {Color.reset} = {Color.green}{table*i}{Color.reset}")

print ("{}{:=^50}{}".format(Color.redBold, emojize("CHALLENGE 49 END" + Emoji.challenge), Color.reset))