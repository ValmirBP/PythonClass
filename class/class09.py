from cmath import phase
from itertools import count
from emoji import emojize

print("{:=^50}".format(emojize(" CLASS 09  :snake: ")))
print("{: ^50}".format("manipulating strings"))

phrase = 'Curso em Video Python'
#  C u r s o   e m   V    i   d  e  o     P   y   t   h  o  n
#  0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16  17  18  19  20

# cutting

print(phrase[9])  # V
print(phrase[9:13])  # Vide
print(phrase[9:14])  # Video
print(phrase[9:21])  # Video Python
print(phrase[9:21:2])  # VdoPto
print(phrase[9:])  # Video Python
print(phrase[:20])  # Curso em Video Pytho
print(phrase[9::3])  # VePh

# analising

print(len(phrase))  # 21
print(phrase.count("o"))  # 3 times of o appear
print(phrase.count("o", 0, 13))  # 1 from 0 to 13 there is only 1 "o" string
print(phrase.find("deo"))  # witch position it is?
print(phrase.find("Android"))  # there is no exprention on this
print("Curso" in phrase)  # is there exprention on this?

# Tranforming

print(phrase.replace('Python', 'Android'))
print(phrase.upper())
print(phrase.lower())
print(phrase.capitalize())
print(phrase.title())

phrase = "   Aprendendo Phythom  "

print(phrase.strip())
print(phrase.rstrip())
print(phrase.lstrip())

# dividing

phrase = 'Curso em Video Python'
print(phrase.split()) # ler split

# Junction
print('-'.join(phrase.split())) # ler split


print("{:=^50}".format(emojize(" CLASS 09 END :snake: ")))
