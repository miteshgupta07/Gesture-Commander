# Import necessary libraries
from pynput.keyboard import Key, Controller
import time

# Initialize the keyboard controller
controller = Controller()

# Function to increase the volume
def Volume_Up():
    controller.press(Key.up)      # Simulate pressing the 'up' arrow key
    controller.release(Key.up)    # Simulate releasing the 'up' arrow key

# Function to decrease the volume
def Volume_Down():
    controller.press(Key.down)    # Simulate pressing the 'down' arrow key
    controller.release(Key.down)  # Simulate releasing the 'down' arrow key

# Function to skip forward
def Forward():
    controller.press(Key.shift)    # Simulate pressing the 'shift' key
    controller.press(Key.right)    # Simulate pressing the 'right' arrow key
    controller.release(Key.shift)  # Simulate releasing the 'shift' key
    controller.release(Key.right)  # Simulate releasing the 'right' arrow key

# Function to skip backward
def Backward():
    controller.press(Key.shift)    # Simulate pressing the 'shift' key
    controller.press(Key.left)     # Simulate pressing the 'left' arrow key
    controller.release(Key.shift)  # Simulate releasing the 'shift' key
    controller.release(Key.left)   # Simulate releasing the 'left' arrow key

# Function to pause or resume playback
def Pause_Resume():
    controller.press(Key.space)    # Simulate pressing the 'space' key
    controller.release(Key.space)  # Simulate releasing the 'space' key
    time.sleep(0.25)               # Short delay to ensure the key press is registered
