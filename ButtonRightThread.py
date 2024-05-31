import ThymioStates
from ThymioStates import ThymioStates

from EventListThread import EventListThread

from tdmclient import ClientAsync, aw

import numpy as np

import fonctions

import threading
import time
import queue


class ButtonRightThread(threading.Thread):
    def __init__(self, event_list_thread, robot):
        super(ButtonRightThread, self).__init__()
        self.event_list_thread = event_list_thread
        self.shutdown_event = threading.Event()  # Event to signal shutdown

        self.robot = robot

    def run(self):
        self.stop = False
        while not self.stop:

            color = [0,0,24,0,0,0,0,0]
            self.robot.setLEDCircle(color) 

            self.robot.setLEDTop([32,32,0])

            print("in Button Right")


    def kill(self):
        self.stop = True