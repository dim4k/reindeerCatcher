# Created by Antoine Kim
# 08/12/2018
# ---------------------------------
# Catch every reindeer on Dealabs !
# ---------------------------------
#
# 1 - Put Dealabs in fullscreen on your favorite browser (resolution need to be 1920x1080)
# 2 - Run the script
# 3 - Move your mouse to stop
#
# Base on Chris Kiehl code :
# https://code.tutsplus.com/tutorials/how-to-build-a-python-bot-that-can-play-web-games--active-11117

from PIL import ImageGrab
import win32api
import win32con
import time
from numpy import *

# Globals
# ------------------
x_pad = 0
y_pad = 0
reindeer_coord = (1584, 1017)
exitModal_coord = (1879, 885)


def screen_grab():
    screen = (x_pad + 0, y_pad + 0, x_pad + 1920, y_pad + 1080)
    im = ImageGrab.grab(screen)
    return im


def left_click():
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    time.sleep(.1)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)


def mouse_pos(cord):
    win32api.SetCursorPos((x_pad + cord[0], y_pad + cord[1]))


def get_cords():
    x, y = win32api.GetCursorPos()
    x = x - x_pad
    y = y - y_pad
    print x, y


def is_on_known_coord():
    x, y = win32api.GetCursorPos()
    x = x - x_pad
    y = y - y_pad
    return (x == reindeer_coord[0] and y == reindeer_coord[1]) or (x == exitModal_coord[0] and y == exitModal_coord[1])


def click_on_coord(coord):
    mouse_pos(coord)
    left_click()


def start_script():
    # Initialize cursor position
    mouse_pos(reindeer_coord)
    print('\033[93m' + 'Let the hunt begin !')
    i = 0
    # Script will loop without any user mouse movement
    while is_on_known_coord():
        im = screen_grab()
        # Check if pixel color is not matching the dealabs default background
        if im.getpixel(reindeer_coord) != (233, 234, 237):
            i += 1
            click_on_coord(reindeer_coord)
            time.sleep(2)
            click_on_coord(exitModal_coord)
            print('\033[92m' + 'Reindeer captured !')
        time.sleep(2)
    print('\033[93m' + 'Script stopped by user input')
    print('\033[93m' + '=== Total number of reindeer : ' + str(i) + ' ===')


def main():
    start_script()


if __name__ == '__main__':
    main()
