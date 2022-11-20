import pyautogui
import threading
import numpy as np
import time
import keyboard

import src.shared.controlCommands as controls
import src.consts.GuiScreenshots as gs

GUI_SCREENS = gs.GuiScreenshot

navigation = False
failed_navigation = 0
subscribtion = False


def run_navigation_cycle():
    while navigation:
        continue_navigation()
        time.sleep(3)


def collect():
    controls.click(950, 150)
    time.sleep(1.5)
    controls.click(1700, 1000)
    time.sleep(1.5)
    controls.click(0, 700)
    time.sleep(1.5)
    controls.click(425, 180)
    time.sleep(1.5)
    return True


def continue_navigation():
    global failed_navigation
    if not controls.find_and_click(GUI_SCREENS.navigation_paused):
        failed_navigation += 1
    else:
        failed_navigation = 0


def start_navigation():
    global navigation
    navigation = True
    global failed_navigation
    failed_navigation = 0
    threading.Thread(target=run_navigation_cycle).start()


def stop_navigation():
    global navigation
    navigation = False


def is_navigation_broken():
    global subscribtion
    subscribtion = True
    while subscribtion:
        if failed_navigation > 5:
            unsubscribe()
            return True
        time.sleep(10)

    return False


def unsubscribe():
    global subscribtion
    subscribtion = False
