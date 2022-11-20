from pyautogui import *
import pyautogui
import threading
import numpy as np
import time
import keyboard

import src.mods.navigator as navigator

import src.shared.controlCommands as controls
import src.consts.GuiScreenshots as gs

GUI_SCREENS = gs.GuiScreenshot

isFighting = False
isCollectingMode = False
combatMode = False


def check_skill(image, key):
    loc = pyautogui.locateOnScreen(controls.get_image_path(image), grayscale=True, confidence=.7)
    if loc is not None:
        keyboard.press_and_release(key)
        sleep(0.1)


def check_skills():
    while combatMode:
        check_skill(GUI_SCREENS.nec_second_spell, '2')
        check_skill(GUI_SCREENS.activated_golem, '2')
        check_skill(GUI_SCREENS.nec_first_spell, '1')
        check_skill(GUI_SCREENS.nec_third_spell, '3')
        check_skill(GUI_SCREENS.nec_forth_spell, '4')
        check_skill(GUI_SCREENS.health_checkpoint, 'q')
        navigator.continue_navigation()
        time.sleep(5)


def check_collecting():
    if isCollectingMode:
        stop_combat_mode()
        navigator.stop_navigation()
        if navigator.collect():
            start_combat_mode(True)
            navigator.start_navigation()


def support_aa():
    is_aa_activated = False
    global isFighting
    while combatMode:
        fight_status = pyautogui.locateOnScreen(controls.get_image_path(GUI_SCREENS.fight_status), grayscale=True, confidence=.85)
        if fight_status is None or combatMode is False:
            isFighting = False
            if is_aa_activated and combatMode:
                navigator.start_navigation()
                if isCollectingMode:
                    check_collecting()
            is_aa_activated = False
        elif not is_aa_activated:
            is_aa_activated = True
            isFighting = True
            navigator.stop_navigation()
            threading.Thread(target=aa_cycle).start()
        sleep(1)


def aa_cycle():
    while isFighting and combatMode:
        keyboard.press_and_release('space')
        sleep(0.5)


def start_combat_mode(is_collecting=False):
    global combatMode
    if not combatMode:
        combatMode = True
        global isCollectingMode
        isCollectingMode = is_collecting
        threading.Thread(target=check_skills).start()
        threading.Thread(target=support_aa).start()


def stop_combat_mode():
    global combatMode
    combatMode = False
