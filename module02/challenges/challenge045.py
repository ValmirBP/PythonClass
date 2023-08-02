from secrets import choice
from time import sleep
from emoji import emojize
from ClassColorsEmojis import *
import pygame


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

audioPath=r"C:\Users\valmi\OneDrive\Documents\Enviroment\PythonClass\module02\challenges\sounds"

def playSound  (sound):
    pygame.mixer.init()
    pygame.mixer.music.load(audioPath + sound)
    pygame.mixer.music.play(loops=1,start=0.0)
    input()
    pygame.mixer.music.stop()

print("{}{:=^100}{}".format(colorDic['greenBold'], emojize("CHALLENGE 45 :crossed_swords:"), colorDic['end']))
print("{}write a software that play{}" "{} Jokeeeeeen pooow....{}".upper().format(colorDic['blueBold'], colorDic['end'], colorDic['redBold'], colorDic['end']))
x= 1
sleep(1)
print(x)

x= x+1
sleep(1)
print(x)

x= x+1
sleep(1)
print(x)
print("GOO!\n")

jkpLst= ["1","2","3"]
pc= int(choice(jkpLst))

while True:
    try:
        player= int(input("choose \n[1]rock \n[2]Paper \n[3]Scissors: \n"))
        break
    except ValueError :
        print(Color.redBold, "Invalid Input",Color.reset)

if player == pc:
    sound = "\smb_stage_clear.wav"
    print(pc, "\n")
    print("{}again{}".upper().format(colorDic['blueBold'], colorDic['end']))
    playSound(sound)

elif player > pc:
    sound = "\smb_stage_clear.wav"
    print(pc, "\n")
    print("{}You win!!!{}".upper().format(colorDic['greenBold'], colorDic['end']))
    playSound(sound)
elif player < pc:
    sound = "\smb_gameover.wav"
    print(pc, "\n")
    print("{}You loose!!!{}".upper().format(colorDic['redBold'], colorDic['end']))
    playSound(sound)

print("{}{:=^100}{}".format(colorDic['greenBold'], emojize("CHALLENGE 45 END :crossed_swords:"), colorDic['end']))