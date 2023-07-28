from emoji import emojize
from ClassColorsEmojis import *

print ("{:=^50}".format(emojize("CHALLENGE 043"+ Emoji.challenge)))

print(f"{Color.blue}Write a software that ask for the user his tall and his weight and calculate the IMC{Color.reset}")

print(f"""{Color.blue}following the instructions
less than 18,5 thinness
from 18,5 to 24,9 normal
from 25 to 29,9 overweight
from 30 to 34,9 obesity first grade
from 35 to 39,9 obesity second grade
bigger than 40 obesity third grade{Color.reset}""")

while True:
    try:
        weight = float(input("Type here the  weight: ").strip())
        tall = float(input("Type here the Tall: ").strip())
        imc = weight / (tall * tall)
        break
    except ValueError:
        print(f"{Color.redBold}\nInvalid input\n{Color.reset}")

print("Your IMC is {:.2f}".format(imc))

if imc < 18.5:
    print("Thinness".upper().format(Color.yellowBold, Color.reset))

elif imc > 18.5 and imc <= 24.9:
    print("Normal".upper().format(Color.greenBold, Color.reset))

elif imc > 25 and imc <= 29.9:
    print("{}overweight{}".upper().format(Color.redBold, Color.reset))

elif imc > 30 and imc <= 34.9:
    print("{}obesity first grade{}".upper().format(Color.redBold, Color.reset))

elif imc > 35 and imc <= 39.9:
    print("{}obesity second grade{}".upper().format(Color.redBold, Color.reset))

elif imc > 40:
    print("{}obesity second grade{}".upper().format(Color.redBold, Color.reset))

print ("{:=^50}".format(emojize("CHALLENGE 043 END"+ Emoji.challenge)))