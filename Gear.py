from Tools import GearADB
from PIL import Image
import numpy as np
import time


gdb = GearADB()


class GearCommander(object):
    """docstring for GearCommander"""
    def __init__(self):
        super(GearCommander, self).__init__()


class Moil(object):
    """docstring for Moil"""
    def __init__(self):
        self.button_init()
        self.file_init()

    def button_init(self):
        self.next_botton = (2544, 1300)
        self.start_mission_botton = (2800, 1225)

    def file_init(self):
        self.next_pic_path = r'picref\next.png'
        self.start_pic_path = r'picref\start_mission.png'
        self.next_pic_img = Image.open(self.next_pic_path).convert('L')
        self.start_pic_img = Image.open(self.start_pic_path).convert('L')
        self.next_pic_np = np.array(self.next_pic_img)
        self.start_pic_np = np.array(self.start_pic_img)

        self.next_pic_region = (1, 85, 1700, 297)
        self.start_pic_region = (2020, 587, 2260, 754)

    def press_next(self):
        print('点击 <下一步>.')
        gdb.tap(self.next_botton)

    def press_start_mission(self):
        print('点击 <开始任务>.')
        gdb.tap(self.start_mission_botton)

    def detect_screen(self):
        print('正在检测屏幕.')
        screen_img = gdb.screenshot()

        crop_next_pic_region = screen_img.crop(self.next_pic_region)
        crop_start_pic_region = screen_img.crop(self.start_pic_region)

        crop_next_pic_region_np = np.array(crop_next_pic_region)
        crop_start_pic_region_np = np.array(crop_start_pic_region)

        next_seem = self.matseem(crop_next_pic_region_np, self.next_pic_np)
        start_seem = self.matseem(crop_start_pic_region_np, self.start_pic_np)

        print(f'下一步的相似度为：{next_seem}')
        print(f'开始的相似度为：{start_seem}')

        if next_seem < 60:
            self.press_next()

        if start_seem < 60:
            self.press_start_mission()

    def matseem(self, mat_1, mat_2):
        return (mat_1 - mat_2).sum() // (mat_1.size)


if __name__ == '__main__':
    mol = Moil()
    while True:
        mol.detect_screen()
        time.sleep(5)
        print()

