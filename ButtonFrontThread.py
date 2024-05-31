import ThymioStates
from ThymioStates import ThymioStates

from EventListThread import EventListThread

from tdmclient import ClientAsync, aw

import numpy as np

import fonctions

import threading
import time
import queue


class ButtonFrontThread(threading.Thread):
    def __init__(self, event_list_thread, robot):
        super(ButtonFrontThread, self).__init__()
        self.event_list_thread = event_list_thread
        self.shutdown_event = threading.Event()  # Event to signal shutdown

        self.client = ClientAsync()
        self.node = aw(self.client.wait_for_node())

        self.robot = robot

    def run(self):
        self.stop = False
        while not self.stop:

            print("in Button Front")

            color = [24,0,0,0,0,0,0,0]
            self.robot.setLEDCircle(color) 

            self.robot.setLEDTop([0,32,0])

            fonctions.no_costume(self.robot, self.node, motor_speed=0)

            # # Simulate processing events from the event list
            # with self.event_list_thread.event_list_lock:
            #     if self.event_list_thread.event_list:
            #         event = self.event_list_thread.event_list.pop()
            #         print("Event processed:", event)
            # time.sleep(2)

    def kill(self):
        self.stop = True