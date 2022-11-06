import keyboard
import time
from pynput.keyboard import Key, Controller

keycup = Controller()


def press(*keys):
    for key in keys:
        keycup.press(key)
        time.sleep(0.5)


# Start from station !don't use on planets
while True:
    if keyboard.is_pressed("ctrl + 1"):
        time.sleep(1)
        press(Key.space, 'd', Key.space, 'd', Key.space, 's', 's', Key.space)
        time.sleep(70)
# Start from station !use on planets only
    if keyboard.is_pressed("ctrl + 2"):
        time.sleep(1)
        press(Key.space, 'd', Key.space, 'd', Key.space, 's', 's', Key.space)
        time.sleep(70)
# Start in free space
    if keyboard.is_pressed("ctrl + 3"):
        time.sleep(1)
# Stops the script
    if keyboard.is_pressed("f1"):
        break
