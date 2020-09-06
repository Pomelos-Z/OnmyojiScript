import random
import time
import pyautogui
from PIL import Image as IMTool
from helper import get_point, do_click_screen


class Driver(object):
    def __init__(self, i=1):
        self.index = i
        self.flag = 0
        self.begin_img = "./images/begin.png"
        self.end_img = "./images/xun.png"

    def click_to_begin(self, result):
        start_pic_x, start_pic_y = IMTool.open(self.begin_img).size
        click_x = result[0] + random.randint(-int(start_pic_x / 2), int(start_pic_x / 2))
        click_y = result[1] + random.randint(-int(start_pic_y / 2), int(start_pic_y / 2))
        pyautogui.click(x=click_x, y=click_y, duration=0.2)

    def start(self):
        while True:
            result = get_point(self.begin_img)
            if result is not None:
                self.flag += 1
                if self.flag >= 10:
                    break
                self.click_to_begin(result)
            elif get_point(self.end_img) is not None:
                print("{} 第{}次御魂结束".format(time.strftime("%H:%M:%S"), self.index))
                self.index += 1
                self.flag = 0
                do_click_screen()
            else:
                continue


if __name__ == '__main__':
    Driver().start()
