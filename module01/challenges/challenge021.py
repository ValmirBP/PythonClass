import pygame
from emoji import emojize

print("{:=^50}\n".format(emojize(" CHALLENGE 021 :crossed_swords:  ")))

print(" Write a softare that read an MP3 audio\n")
audioPath=r"C:\Users\valmi\Documents\enviroment\studies\self_studies\python\PythonClass\module01\challenges\Challenge21.mp3"
pygame.mixer.init()
pygame.mixer.music.load(audioPath)
pygame.mixer.music.play(loops=0,start=0.0)
input()
pygame.mixer.music.stop()

print("{:=^50}".format(emojize(" CHALLENGE 021 :2nd_place_medal:  ")))