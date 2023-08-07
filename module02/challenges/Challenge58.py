from random import randint
from emoji import emojize
import pygame
from ClassColorsEmojis import *


def play_sound(sound):
    pygame.mixer.init()
    pygame.mixer.music.load(sound)
    pygame.mixer.music.play(loops=0,start=0.0)
    input()
    pygame.mixer.music.stop()

audioWin=r"C:\Users\valmi\OneDrive\Documents\Enviroment\PythonClass\module02\challenges\sounds\Mario_Bros_Up_Sound.mp3"
audioLose=r"C:\Users\valmi\OneDrive\Documents\Enviroment\PythonClass\module02\challenges\sounds\smb_pipe.wav"
audioGameOver=r"C:\Users\valmi\OneDrive\Documents\Enviroment\PythonClass\module02\challenges\sounds\smb_stage_clear.wav"

print(Color.green, "\n"," CHALLENGE 58 ".center(50, emojize(Emoji.axe)),Color.reset, "\n")

print(Color.cyan,f"""Improve the CHALLENGE 028 when you need to guess the number between 0 and 10,
but the gamer need do the right guess  to end  the game""", Color.reset)

number = randint(0,10)
guess = 0
name = input("Type here your name: ")
tries = 0
print(Color.green,"Try to  guess the number", Color.reset)

while guess != number:
    try:
        tries += 1
        guess = int(input("\n Type here he number: "))
    except ValueError:
            print(Color.red,"invalid value", Color.reset)
            print("Please input a number.")
            play_sound(audioLose)
    else:
        if guess == 0:
            print("Please input a number.")
            play_sound(audioLose)
        elif guess > 10:
            print(Color.red,"Sorry wrong guess. your guess mus be between 0 and 10 ", Color.reset)
            play_sound(audioLose)
        elif guess < number:
            print(Color.red,"Sorry wrong guess. Try something BIGGER", Color.reset)
            play_sound(audioLose)
        elif guess > number:
            print(Color.red,"Sorry wrong guess. Try something SMALLER", Color.reset)
            play_sound(audioLose)
        else:
            play_sound(audioWin)
            print(Color.green,f"congratulations!!! {name}, you got it with {tries} tries")
            play_sound(audioGameOver)

print(Color.green, "\n"," CHALLENGE 58 END ".center(50, emojize(":axe:")),Color.reset, "\n")