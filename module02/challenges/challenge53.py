from ast import If
from posixpath import split
from emoji import emoji_list, emojize


colorDic = {
     'bold'          : '\033[1m'
    ,'red'          : '\033[31m'
    ,'green'        : '\033[32m'
    ,'yellow'       : '\033[33m'
    ,'blue'         : '\033[34m'
    ,'redBold'      : '\033[1;31m'
    ,'greenBold'    : '\033[1;32m'
    ,'yellowBold'   : '\033[1;33m'
    ,'blueBold'     : '\033[1;34m'
    ,'end'          : '\033[m'
}

print ("{}{:=^50}{}".format(colorDic['redBold'], emojize("CHALLENGE 52 :crossed_swords:  "), colorDic['end']))

print("{}Write a software that ask to the user and check if tis a palindrome {}".format(colorDic['blueBold'],colorDic['end']))

phrase = str(input("Type here a phrase: ")).strip().upper()
words = phrase.split()
joining = ''.join(words)
invert = ''

for letter in range(len(joining) - 1,-1,-1 ):
    invert += joining[letter]
if invert == joining:
    print("The word {}{}{} is a ".format(colorDic['yellowBold'],joining,colorDic['end']) + "{}Palindrome{}".upper().format(colorDic['greenBold'],colorDic['end']))
else:
    print("The word {}{}{} is".format(colorDic['yellowBold'],joining,colorDic['end']) + " {}not{} a ".upper().format(colorDic['redBold'],colorDic['end'])+ "{}Palindrome{}".upper().format(colorDic['greenBold'],colorDic['end']))


    

print ("{}{:=^50}{}".format(colorDic['redBold'], emojize("CHALLENGE 52 END :crossed_swords:  "), colorDic['end']))