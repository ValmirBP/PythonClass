import sys
import pyautogui
import time

currentTime = time.strftime("%H:%M:%S")
print(currentTime)
endTime = input ("Type here the time you  want to  stop HH:MM:SS: ")
pyautogui.FAILSAFE = True

while (currentTime < endTime):
    try:
        currentTime = time.strftime("%H:%M:%S")
        print(currentTime)

        pyautogui.moveTo(916,438,duration=0.15)
        # pyautogui.sleep (0.50)
        # print(pyautogui.position())

        pyautogui.moveTo(916,338,duration=0.15)
        # pyautogui.sleep (1)
        # print(pyautogui.position())

        pyautogui.moveTo(816,338,duration=0.15)
        # pyautogui.sleep (1)
        # print(pyautogui.position())

        pyautogui.moveTo(816,438,duration=0.15)
        # pyautogui.sleep (1)
        # print(pyautogui.position())

        pyautogui.moveTo(916,438,duration=0.15)
        # pyautogui.sleep (1)
        # print(pyautogui.position())

    except KeyboardInterrupt:
        sys.exit()