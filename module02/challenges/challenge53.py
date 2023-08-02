from emoji import emojize
from ClassColorsEmojis import *

print ("{}{:=^50}{}".format(Color.redBold, emojize("CHALLENGE 52 " + Emoji.challenge), Color.reset))

print(f"{Color.cyan}Write a software that ask to the user and check if it´s a palindrome {Color.reset}")

phrase = str(input("Type here a phrase: ")).strip().upper()
words = phrase.split()
joining = ''.join(words)
invert = ''

for letter in range(len(joining) - 1,-1,-1 ):
    invert += joining[letter]
if invert == joining:
    print(f"The word {Color.yellowBold}{phrase}{Color.reset} is a {Color.greenBold}Palindrome{Color.reset}")
else:
    print(f"""The word {Color.yellowBold}{phrase}{Color.reset} is {Color.redBold}NOT{Color.reset}
a {Color.greenBold} Palindrome {Color.reset}""")




print ("{}{:=^50}{}".format(Color.redBold, emojize("CHALLENGE 52 END" + Emoji.challenge), Color.reset))