from pynput.keyboard import Key,Controller
import time

controller=Controller()

def Volume_Up():
    controller.press(Key.up)
    controller.release(Key.up)
    

def Volume_Down():
    controller.press(Key.down)
    controller.release(Key.down)
    

def Forward():
    controller.press(Key.shift)
    controller.press(Key.right)
    controller.release(Key.shift)
    controller.release(Key.right)
    

def Backward():
    controller.press(Key.shift)
    controller.press(Key.left)
    controller.release(Key.shift)
    controller.release(Key.left)
    

def Pause_Resume():
    controller.press(Key.space)
    controller.release(Key.space)
    time.sleep(0.25)
    