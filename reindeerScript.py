# Created by Antoine Kim
# 08/12/2018
# ---------------------------------
# Catch every reindeer on Dealabs !
# ---------------------------------
#
# Based on Chris Kiehl code :
# https://code.tutsplus.com/tutorials/how-to-build-a-python-bot-that-can-play-web-games--active-11117

from PIL import ImageGrab
import win32api
import win32con
import time

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
    return x, y


def click_on_coord(coord):
    current_coord = get_cords()
    mouse_pos(coord)
    left_click()
    mouse_pos(current_coord)


def scroll_on_coord(coord, distance):
    current_coord = get_cords()
    mouse_pos(coord)
    win32api.mouse_event(win32con.MOUSEEVENTF_WHEEL, 0, 0, distance, 0)
    mouse_pos(current_coord)


def refresh(coord):
    current_coord = get_cords()
    mouse_pos(coord)
    left_click()
    win32api.keybd_event(0x74, 0, 0, 0)
    time.sleep(.05)
    win32api.keybd_event(0x74, 0, win32con.KEYEVENTF_KEYUP, 0)
    mouse_pos(current_coord)


def start_script():
    print('\033[93m' + 'Let the hunt begin !')
    i = 0
    # Script need to be stopped
    while 1:
        i += 1
        im = screen_grab()
        # Check if pixel color is not matching the dealabs default background
        if im.getpixel(reindeer_coord) != (233, 234, 237) and im.getpixel(reindeer_coord) != (255, 255, 255):
            click_on_coord(reindeer_coord)
            time.sleep(1)
            refresh(reindeer_coord)
            print('\033[92m' + '=== Reindeer captured ===')
            # Just to be sure that the page is fully reload
            time.sleep(3)

        # Every approx half hour go on page and scroll
        if i % 20 == 0:
            print('\033[93m' + 'Auto-scroll down')
            scroll_on_coord(reindeer_coord, -2000)

        if i % 30 == 0:
            print('\033[93m' + 'Auto-scroll up')
            scroll_on_coord(reindeer_coord, 1500)

        # Every approx hour go refresh the page
        if i % 150 == 0:
            print('\033[93m' + 'Auto-refresh')
            scroll_on_coord(reindeer_coord, -2000)
            click_on_coord(reindeer_coord)
            time.sleep(2)
            refresh(reindeer_coord)

        time.sleep(2)


def main():
    print('\033[95m' + 'Put Dealabs in fullscreen on your main screen (1920x1080)')
    print('\033[95m' + 'Don''t let any other program go in front of your web browser in the lower right 1/4 of your screen')
    print('\033[95m' + 'Press CTRL+C on this terminal to kill the process')
    raw_input('\033[91m' + '*** Press any key to start ***')
    start_script()


if __name__ == '__main__':
    main()
