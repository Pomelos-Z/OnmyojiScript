import random
import time
import win32gui
import pyautogui


def get_game_window_size():
    game = u'阴阳师-网易游戏'
    handle = win32gui.FindWindow(0, game)
    if handle == 0:
        return None
    else:
        window_size = win32gui.GetWindowRect(handle)
        return window_size


def get_point(pic):
    point = None
    try:
        point = pyautogui.locateCenterOnScreen(pic)
    except Exception:
        pass
    return point


def do_click_screen():
    left, up, right, down = get_game_window_size()
    end_x = random.randint(left + 10, round(left + (right - left) / 6 * 1))
    end_y = random.randint(round(up + (down - up) / 5 * 3), round(down - (down - up) / 5 * 1))
    for i in range(8):
        pyautogui.click(x=end_x, y=end_y, duration=0.2)
        time.sleep(0.2)
