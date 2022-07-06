import time
import threading
from pynput.mouse import Button, Controller
from pynput.keyboard import Listener, KeyCode
import os 

os.system('cls' if os.name == 'nt' else 'clear')

start = time.time()
elapsed_time = time.time() - start

delay = 1
button = Button.left
start_stop_key = KeyCode(char='a')
stop_key = KeyCode(char='b')

class ClickMouse(threading.Thread):
    def __init__(self, delay, button):
        super(ClickMouse, self).__init__()
        self.delay = delay
        self.button = button
        self.running = False
        self.program_running = True

    def start_clicking(self):
        self.running = True
  
    def stop_clicking(self):
        self.running = False
  
    def exit(self):
        self.stop_clicking()
        self.program_running = False

    def run(self):
        while self.program_running:
            while self.running:
                mouse.position = (119, 943) # Blizzard
                mouse.click(self.button)
                time.sleep(self.delay)
                mouse.position = (962, 410) # Battlegrounds
                mouse.click(self.button)
                time.sleep(self.delay)
                mouse.position = (1466, 851) # Play
                mouse.click(self.button)
                time.sleep(self.delay)
                mouse.position = (954, 658) # Couldn't Join Error
                mouse.click(self.button)
                time.sleep(self.delay)
                
            time.sleep(0.1)

mouse = Controller()
click_thread = ClickMouse(delay, button)
click_thread.start()

def on_press(key):
    if key == start_stop_key:
        if click_thread.running:
            click_thread.stop_clicking()
        else:
            click_thread.start_clicking()

    elif key == stop_key:
            click_thread.exit()
            listener.stop()
            elapsed_time = time.time() - start
            os.system('cls' if os.name == 'nt' else 'clear')
            print('Elapsed Time:', time.strftime("%H:%M:%S", time.gmtime(elapsed_time)))
  
with Listener(on_press=on_press) as listener:
    listener.join()
