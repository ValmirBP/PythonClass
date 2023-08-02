from emoji import emojize
from ClassColorsEmojis import *

print ("{}{:=^50}{}".format(Color.redBold, emojize("CHALLENGE 47 :crossed_swords:  "), Color.reset))
print("{}Write a software that show all pairs numbers from 1 to 50{}".format(Color.yellowBold,Color.reset))

for i in range (1,51):
    if i%2 == 0 :
        print( i,end=' ')

print("\n\n other way  to solve it:\n".upper())

for i in range (2,51, 2):
    print( i,end=' ')

print ("\n{}{:=^50}{}".format(Color.redBold, emojize("CHALLENGE 47 END :crossed_swords:"), Color.reset))