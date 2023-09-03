from random import randint
from ClassColorsEmojis import *
from emoji import emojize

print ("{}{:=^50}{}".format(Color.redBold,emojize("CHALLENGE 77 " + Emoji.challenge),Color.reset))

print(f"""\n{Color.cyan} Create a program that has a tuple with several words (don't use accents).
After that, you must show, for each word, which are its vowels.
{Color.reset}\n""")

words = ("apple", "banana", "orange", "grape", "pear",
            "car", "bus", "bike", "train", "airplane",
            "cat", "dog", "elephant", "lion", "giraffe",
            "book", "pen", "paper", "computer", "keyboard")
vowels = 'aeiou'
for word in words:
    print(f'\n\nOn {word} there is: ',end='')
    for letter in  word:
        if letter.lower() in vowels:
            print(f'{letter}',end=' ')


print ("\n{}{:=^50}{}".format(Color.redBold,emojize("CHALLENGE 77 END" + Emoji.challenge),Color.reset))
