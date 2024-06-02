import time
from pynput.keyboard import Controller,Key

controller=Controller()
time.sleep(2)
# controller.press(Key.shift)
controller.press(Key.up)
# controller.release(Key.shift)
controller.release(Key.up)
