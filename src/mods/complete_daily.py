import time

import src.shared.controlCommands as controls
import src.consts.GuiScreenshots as gs

GUI_SCREENS = gs.GuiScreenshot


def run():
    print('complete daily')
    is_daily_done = False
    is_bounties_quarter = False
    is_claim_reward = False

    while 1:
        if is_daily_done is False:
            is_daily_done = controls.find_and_click(GUI_SCREENS.bounties)
        elif is_bounties_quarter is False:
            is_bounties_quarter = controls.find_and_click(GUI_SCREENS.bounties_quartermaster)
        elif is_claim_reward is False:
            is_claim_reward = controls.find_and_click(GUI_SCREENS.claim_reward)
        elif is_claim_reward:
            return True
        time.sleep(5)
