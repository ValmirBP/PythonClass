from distutils.command.clean import clean
from turtle import clear
from emoji import emojize


print("{:=^50}". format(emojize("CLASS 11 :snake:")))
print("{: ^50}". format("Using colors\n"))

"""
pattern ansi colors for python 

ANSI pattern

\033[style;text;back]m
style           text           back
0 = none        30 = white     40 = white
1 = bold        31 = red       41 = red
4 = underline   32 = green     42 = green
7 = negative    33 = yellow    43 = yellow
                34 = blue      44 = blue
                35 = purple    45 = purple
                36 = caine     46 = caine
                37 = gray      47 = gray
"""

print("\033[0;30;40m {: ^45} \033[m".format("TEST"))
print("\033[m {: ^45} \033[m ".format("TEST"))

text = "TEST"
print("{} {: ^45} {}".format("\033[1;35m", text, "\033[m"))

colors = {
'clear'     : '\033[m'
,'blue'     : '\033[34m'
,'yellow'   : '\033[33m'
,'negative' : '\033[7m'
}

print("{} {: ^45} {} ".format(colors['blue'], text, colors['clear']))
print("{} {: ^45} {} ".format(colors["yellow"], text, colors["clear"]))
print("{} {: ^45} {} ".format(colors["negative"], text, colors["clear"]))
print("{:=^50}". format(emojize("CLASS 11 END :snake:")))
