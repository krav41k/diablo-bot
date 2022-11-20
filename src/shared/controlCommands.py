from pyautogui import *
import pyautogui
import time

import win32api
import win32con


def click(x: int, y: int):
    win32api.SetCursorPos((x, y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    time.sleep(1)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)


def get_image_path(image_name):
    return 'assets/screenshots/' + image_name


def find_and_click(image, confidence=.8):
    image_path = get_image_path(image)
    print(image_path)
    image_loc = pyautogui.locateOnScreen(image_path, grayscale=True, confidence=confidence)
    if image_loc is not None:
        x = int(image_loc.left + (image_loc.width / 2))
        y = int(image_loc.top + (image_loc.height / 2))
        click(x, y)
        return True
    else:
        return False
