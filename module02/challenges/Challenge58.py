from random import randint
from emoji import emojize
import pygame

class color:
    black = '\033[30m'
    red = '\033[31m'
    green = '\033[32m'
    orange = '\033[33m'
    blue = '\033[34m'
    purple = '\033[35m'
    cyan = '\033[36m'
    lightGrey = '\033[37m'
    darkGrey = '\033[90m'
    lightRed = '\033[91m'
    lightGreen = '\033[92m'
    yellow = '\033[93m'
    lightBlue = '\033[94m'
    pink = '\033[95m'
    lightCyan = '\033[96m'
    reset = '\033[0m'

def play_sound(sound):
    pygame.mixer.init()
    pygame.mixer.music.load(sound)
    pygame.mixer.music.play(loops=0,start=0.0)
    input()
    pygame.mixer.music.stop()

audioWin=r"C:\Users\valmi\OneDrive\Documents\Enviroment\PythonClass\module02\challenges\Mario_Bros_Up_Sound.mp3"
audioLose=r"C:\Users\valmi\OneDrive\Documents\Enviroment\PythonClass\module02\challenges\smb_pipe.wav"
audioGameOver=r"C:\Users\valmi\OneDrive\Documents\Enviroment\PythonClass\module02\challenges\smb_stage_clear.wav"

print(color.green, "\n"," CHALLENGE 58 ".center(50, emojize(":axe:")),color.reset, "\n")

print(color.cyan,"Improve the CHALLENGE 028 whe you  need to guess the number between 0 and 10, but the gamer need do the right guess  to end  the game ", color.reset)

number = randint(0,10)
guess = 0
name = input("Type here your name: ")
tries = 0
print(color.green,"Try to  guess the number", color.reset)

while guess != number:
    try:
        tries += 1
        guess = int(input("\n Type here he number: "))
    except ValueError:
            print(color.red,"invalid value", color.reset)
            print("Please input a number.")
            play_sound(audioLose)
    else:
        if guess == 0:
            print("Please input a number.")
            play_sound(audioLose)
        elif guess > 10:
            print(color.red,"Sorry wrong guess. your guess mus be between 0 and 10 ", color.reset)
            play_sound(audioLose)
        elif guess < number:
            print(color.red,"Sorry wrong guess. Try something BIGGER", color.reset)
            play_sound(audioLose)
        elif guess > number:
            print(color.red,"Sorry wrong guess. Try something SMALLER", color.reset)
            play_sound(audioLose)
        else:
            play_sound(audioWin)
            print(color.green,f"congratulations!!! {name}, you got it with {tries} tries")
            play_sound(audioGameOver)

print(color.green, "\n"," CHALLENGE 58 END ".center(50, emojize(":axe:")),color.reset, "\n")