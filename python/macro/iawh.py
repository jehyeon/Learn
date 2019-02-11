#####################
# I am working hard #
#####################

import pyautogui
import time

def main():
    while True:
        start_position = pyautogui.position()
        time.sleep(60)
        if start_position == pyautogui.position():
            pyautogui.moveTo(pyautogui.position()[0]+10, pyautogui.position()[1]+10, 0.05)
            pyautogui.moveTo(pyautogui.position()[0]-20, pyautogui.position()[1]-20, 0.05)
            pyautogui.moveTo(pyautogui.position()[0]+10, pyautogui.position()[1]+10, 0.05)
            
if __name__ == '__main__':
    main()