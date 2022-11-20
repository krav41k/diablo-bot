import math
import random

import win32api
from pyautogui import *
import pyautogui
import threading
import time
import keyboard
import numpy as np
import src.shared.controlCommands as controls
import src.consts.GuiScreenshots as gs

import src.mods.complete_daily as complete_daily
import src.mods.make_daily as make_daily
import src.mods.take_daily as take_daily
import src.mods.navigator as navigator
import src.mods.combat as combat

thread_seed = 0
GUI_SCREENS = gs.GuiScreenshot


def run(is_make=False, is_complete=False, is_take=False):
    global thread_seed
    local_seed = thread_seed = random.random()

    if is_make is False:
        if make_daily.run() is True:
            navigator.start_navigation()
            threading.Thread(target=run_save_navigation).start()
            is_collecting = bool(
                pyautogui.locateOnScreen(controls.get_image_path(GUI_SCREENS.collect_quest), grayscale=True,
                                         confidence=.8))
            combat.start_combat_mode(is_collecting)
            daily_done = None
            while daily_done is None:
                daily_done = pyautogui.locateOnScreen(controls.get_image_path(GUI_SCREENS.bounties), grayscale=True,
                                                      confidence=.8)
                print(local_seed)
                if local_seed != thread_seed:
                    return
                sleep(5)

            navigator.stop_navigation()
            navigator.unsubscribe()
            combat.stop_combat_mode()
            sleep(5)
        if complete_daily.run() is True:
            if take_daily.run() is True:
                run()

    elif is_complete is False:
        if complete_daily.run() is True:
            if take_daily.run() is True:
                run()

    elif is_take is False:
        if take_daily.run() is True:
            run()


def run_save_navigation():
    if navigator.is_navigation_broken():
        run()


def main():
    run()
    # combat.start_combat_mode(True)
    # while 1:
        # print(win32api.GetCursorPos())
        # print(random.random())

        # for pos in arr:

        # sleep(5)


threading.Thread(target=main).start()

# def test():
#     while 1:
#         print('test')
#         time.sleep(5)
#         return True

# print(test())
