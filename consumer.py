import time
from helper import get_point, do_click_screen


class Consumer(object):

    def __init__(self):
        self.index = 1
        self.end_img = "./images/jin.png"

    def start(self):
        while True:
            if get_point(self.end_img) is None:
                continue
            else:
                print("{} 第{}次御魂结束".format(time.strftime("%H:%M:%S"), self.index))
                self.index += 1
                do_click_screen()


if __name__ == '__main__':
    Consumer().start()
