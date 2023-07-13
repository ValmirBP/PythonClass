import pygame
from emoji import emojize

print("\n")
print("{:=^50}".format(emojize(" :crossed_swords:  CHALLENGE 021 :crossed_swords:  ")))

print("\n Write a softare that read an MP3 audio")

audioPath=r"C:\Users\valmi\OneDrive\Documents\Enviroment\PythonClass\module01\challenges\Challenge21.mp3"

pygame.mixer.init()
pygame.mixer.music.load(audioPath)
pygame.mixer.music.play(loops=0,start=0.0)
input()
pygame.mixer.music.stop()

print("{:=^50}".format(emojize(" :2nd_place_medal: CHALLENGE 021  END :2nd_place_medal: " )))