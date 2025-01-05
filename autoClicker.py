'''
How to setup python auto clicker:
install python @ python.org
(when stting up install make sure to click add to pathway or else you cant use imports and this script wont work)
open up cmd type these commands: "pip install pyautogui", and "pip install keyboard"
I believe time is preinstalled but if not just pip install it
then your python auto clicker should be ready to use!
script by BetterBrowse~
'''
import pyautogui
import keyboard
import time
def main():
    getClickSpeed()
def getClickSpeed():
    speed = float(input("How fast do you want it to click (sec): "))
    buttonToStart = input("What button do you want to start the auto clicker: ")
    buttonToStop = input("What button do you want to stop the auto clicker: ")
    execute(speed, buttonToStart, buttonToStop)
def execute(t, bStart, bStop):
    go = 0
    while True:
        if go == 1:
            pyautogui.click()
            time.sleep(t)
        if keyboard.is_pressed(bStop):
            if go == 1:
                go-=1
        if keyboard.is_pressed(bStart):
            if go == 0:
                go+=1
main()
        
    
    
