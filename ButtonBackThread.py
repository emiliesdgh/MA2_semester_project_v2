import ThymioStates
from ThymioStates import ThymioStates

from EventListThread import EventListThread

from tdmclient import ClientAsync, aw

import numpy as np

import fonctions

import threading
import time
import queue


class ButtonBackThread(threading.Thread):
    def __init__(self, event_list_thread):
        super(ButtonBackThread, self).__init__()
        self.event_list_thread = event_list_thread
        self.shutdown_event = threading.Event()  # Event to signal shutdown

    def run(self):
        self.stop = False
        while not self.stop:

            print("in Button Back")

            # # Simulate processing events from the event list
            # with self.event_list_thread.event_list_lock:
            #     if self.event_list_thread.event_list:
            #         event = self.event_list_thread.event_list.pop()
            #         print("Event processed:", event)
            # time.sleep(2)

    def kill(self):
        self.stop = True