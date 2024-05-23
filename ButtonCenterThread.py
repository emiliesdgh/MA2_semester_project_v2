import ThymioStates
from ThymioStates import ThymioStates

from EventListThread import EventListThread

from tdmclient import ClientAsync, aw

import numpy as np

import fonctions

import threading
import time
import queue


class ButtonCenterThread(threading.Thread):
    def __init__(self, event_list_thread):
        super(ButtonCenterThread, self).__init__()
        self.event_list_thread = event_list_thread
        self.shutdown_event = threading.Event()  # Event to signal shutdown


    def run(self):
        self.stop = False
        while not self.stop:

            print("in Button Centre")

            fonctions.stop_program(self.event_list_thread.robot, self.event_list_thread.node, motor_speed=0)

            # # Simulate processing events from the event list
            # with self.event_list_thread.event_list_lock:
            #     if self.event_list_thread.event_list:
            #         event = self.event_list_thread.event_list.pop()
            #         print("Event processed:", event)
            time.sleep(2)

    def kill(self):
        self.stop = True

