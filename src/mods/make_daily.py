from pyautogui import *
import pyautogui
import numpy as np
import time

import src.shared.controlCommands as controls
import src.consts.GuiScreenshots as gs

GUI_SCREENS = gs.GuiScreenshot


def run():
    is_daily_list = False
    is_daily_selected = False

    global makeDaily
    makeDaily = True
    while makeDaily:
        if is_daily_list is False:
            is_daily_list = controls.find_and_click(GUI_SCREENS.daily_list)
        elif is_daily_selected is False:
            is_daily_selected = controls.find_and_click(GUI_SCREENS.daily)
            if is_daily_selected is True:
                sleep(15)
                return True
        sleep(5)

        # loc = pyautogui.locateOnScreen(GUI_SCREENS.bounties, grayscale=True, confidence=.8)
