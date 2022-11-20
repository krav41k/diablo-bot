import math

from pyautogui import *
import pyautogui
import numpy as np
import time

import src.shared.controlCommands as controls
import src.consts.GuiScreenshots as gs

GUI_SCREENS = gs.GuiScreenshot

restock_attempts = 0


def run():
    print('take daily')
    is_codex = False
    is_bounties_featured = False
    is_codex_navigate = False
    is_bounty_board = False
    is_quest_accept = False
    is_exit = False
    global takeDaily
    takeDaily = True

    while takeDaily:
        if is_codex is False:
            is_codex = controls.find_and_click(GUI_SCREENS.codex)
        # elif is_bounties_featured is False:
        #     if controls.find_and_click(GUI_SCREENS.bounties_featured) is False:
        #         controls.find_and_click(GUI_SCREENS.codex_bounties)
        #     is_bounties_featured = True
        elif is_codex_navigate is False:
            is_codex_navigate = controls.find_and_click(GUI_SCREENS.codex_navigate)
            if is_codex_navigate is False:
                controls.find_and_click(GUI_SCREENS.codex_claim)
        elif is_bounty_board is False:
            sleep(20)
            controls.click(815, 425)
            is_bounty_board = True
            time.sleep(5)
        elif is_quest_accept is False:
            pos = accept_daily()
            if pos is not None:
                try:
                    x = int(pos[0])
                    y = int(pos[1])
                    controls.click(x, y)
                    is_quest_accept = True
                except:
                    print('pos invalid')
            else:
                global restock_attempts
                if restock_attempts < 3:
                    restock_attempts += 1
                    restock_daily()
                else:
                    print('pizdec bleat')
                    return

        elif is_exit is False:
            is_exit = controls.find_and_click(GUI_SCREENS.exit_cross)
        else:
            return True
        time.sleep(5)


def accept_daily():
    arr = []
    for pos in pyautogui.locateAllOnScreen(controls.get_image_path(GUI_SCREENS.kill), grayscale=True,
                                           confidence=.95):
        arr.append((pos.left, pos.top))
    if len(arr) < 1:
        for pos in pyautogui.locateAllOnScreen(controls.get_image_path(GUI_SCREENS.defeat_description), grayscale=True,
                                               confidence=.95):
            arr.append((pos.left, pos.top))

    for pos in pyautogui.locateAllOnScreen(controls.get_image_path(GUI_SCREENS.collect_description), grayscale=True,
                                           confidence=.95):
        for kill_pos in arr:
            if pos.left - kill_pos[0] >= 0:
                distance = math.sqrt(abs(pos.left - kill_pos[0]) ^ 2 + abs(pos.top - kill_pos[1]) ^ 2)
                if distance < 20:
                    new_arr = []
                    for new_v in arr:
                        if new_v != kill_pos:
                            new_arr.append(new_v)
                    arr = new_arr

    if len(arr) < 1:
        return None

    prev_distance = 9999
    accept_button = (0, 0)
    for pos in pyautogui.locateAllOnScreen(controls.get_image_path(GUI_SCREENS.accept), grayscale=True,
                                           confidence=.95):
        distance = abs(pos.left - arr[0][0])
        if distance < prev_distance:
            prev_distance = distance
            accept_button = (pos.left, pos.top)
    return accept_button


def restock_daily():
    controls.find_and_click(GUI_SCREENS.restock)
