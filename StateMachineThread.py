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
    try:
        robot = ThymioStates()


        # Create an instance of the EventListThread
        event_list_thread = EventListThread(robot)

        # Create instances of StateMachineThread and ActionUpdaterThread
        state_machine_thread = StateMachineThread(event_list_thread)
        action_updater_thread = ActionUpdaterThread()

        # Start all threads
        event_list_thread.start()
        state_machine_thread.start()
        action_updater_thread.start()
        
        # # Add events with different priorities
        # event_list_thread.add_event(2, "Low priority event")
        # event_list_thread.add_event(1, "High priority event")
        # event_list_thread.add_event(3, "Medium priority event")

        # Wait for a while to let the events be processed
        time.sleep(5)

        # Shutdown the event thread
        event_list_thread.kill()
        action_updater_thread.kill()
    except Exception as e:
        print(e)
        event_list_thread.kill()
        action_updater_thread.kill()