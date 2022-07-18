from time import sleep
import pyautogui
from threading import Thread, Lock, Timer
from math import sqrt
class Namierzanie:

 # threading properties
    stopped = True
    lock = None

# movement properites
    targets = []
    window_offset = (0,0)
    window_w = 0
    window_h = 0
    pyautogui.FAILSAFE = False
    
# threading methods

    def __init__(self, window_offset, window_size):
        # create a thread lock object
        self.lock = Lock()
        #update
        self.window_offset = window_offset
        self.window_w = window_size[0]
        self.window_h = window_size[1]
        sleep(3)


    def get_screen_position(self, pos):
        return (pos[0] + self.window_offset[0], pos[1] + self.window_offset[1])

    def targets_ordered_by_distance(self, targets):
        # our character is always in the center of the screen
        my_pos = (self.window_w / 2, self.window_h / 2)
        def pythagorean_distance(pos):
            return sqrt((pos[0] - my_pos[0])**2 + (pos[1] - my_pos[1])**2)
        targets.sort(key=pythagorean_distance)
        return targets

    def update_targets(self, targets):
        
        self.targets = targets
        

    def start(self):
        self.stopped = False
        t = Thread(target=self.run)
        t.start()

    def stop(self):
        self.stopped = True

    # main logic controller
    def run(self):
        
        while not self.stopped:
            if self.targets:
                self.targets = self.targets_ordered_by_distance(self.targets)
                target_pos = self.targets[0]
                screen_x, screen_y = self.get_screen_position(target_pos)
                # move the mouse
                pyautogui.moveTo(x=screen_x + 40, y=screen_y-50)
            
    