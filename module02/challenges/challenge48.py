from emoji import emoji_list, emojize
from ClassColorsEmojis import *

print ("{}{:=^50}{}".format(Color.redBold, emojize("CHALLENGE 48" + Emoji.challenge), Color.reset))
print(f"""{Color.lightBlue}Write a software that show all odd numbers from 1 to 500 and sum the multiplications
of 3 number{Color.reset}""")

sumMutiples = 0
countMultiples = 0

for i in range (1,500):
    if i%2 !=0 and i%3 == 0:
        countMultiples +=1
        sumMutiples +=i
print (Color.blueBold,f"The sum of  all {countMultiples} asked is {sumMutiples}",Color.reset)

print ("\n{}{:=^50}{}".format(Color.redBold, emojize("CHALLENGE 48 END " + Emoji.challenge),Color.reset))