import ThymioStates
from ThymioStates import ThymioStates

from EventListThread import EventListThread

from tdmclient import ClientAsync, aw

import numpy as np

import threading
import time
import queue


class StateMachineThread(threading.Thread):
    def __init__(self, event_list_thread):
        super(StateMachineThread, self).__init__()
        self.event_list_thread = event_list_thread
        self.shutdown_event = threading.Event()  # Event to signal shutdown

    def run(self):
        while True:
            # Simulate processing events from the event list
            with self.event_list_thread.event_list_lock:
                if self.event_list_thread.event_list:
                    event = self.event_list_thread.event_list.pop()
                    print("Event processed:", event)
            time.sleep(2)

class ActionUpdaterThread(threading.Thread):
    def __init__(self):
        super(ActionUpdaterThread, self).__init__()
        self.stop = True

    def run(self):
        self.stop = False
        while not self.stop:
            # Simulate updating actions
            print("Actions updated")
            time.sleep(3)

    def kill(self):
        self.stop = True

if __name__ == "__main__":
    ...