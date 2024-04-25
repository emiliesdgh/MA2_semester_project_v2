import classes
from classes import Thymio

import states
from states import ThymioStates

from tdmclient import ClientAsync, aw

import numpy as np

import threading
import time
import queue

class EventListThread(threading.Thread):
    def __init__(self):
        super(EventListThread, self).__init__()
        self.event_queue = queue.PriorityQueue()
        self.event_list = []
        self.event_list_lock = threading.Lock()  # Lock for protecting access to event list
        self.shutdown_event = threading.Event()  # Event to signal shutdown

    def add_event(self, priority, event_data):
        self.event_queue.put((priority, event_data))
        self.new_event_event.set()  # Signal that a new event is added

    def run(self):
        while not self.shutdown_event.is_set():
            # Wait for the event notification or timeout
            self.new_event_event.wait(timeout=1)
            self.new_event_event.clear()  # Clear the event flag

            # Process events from the priority queue
            while not self.event_queue.empty():
                priority, event_data = self.event_queue.get()
                print("Event added with priority {}: {}".format(priority, event_data))
                # Process the event
                # (For now, we just print it)
                time.sleep(1)  # Simulate event processing

        print("Event thread shutdown.")
        # while True:
        #     # Simulate adding events to the event list
        #     event = time.time()
        #     with self.event_list_lock:
        #         self.event_list.append(event)
        #     print("Event added:", event)
        #     time.sleep(1)

        # while not self.shutdown_event.is_set():
        #     # Simulate adding events to the event list
        #     event = time.time()
        #     with self.event_list_lock:
        #         self.event_list.append(event)
        #     print("Event added:", event)
        #     time.sleep(1)
        #     try:
        #         # Get the next event from the priority queue
        #         priority, event_data = self.event_queue.get(timeout=1)
        #         print("Event added with priority {}: {}".format(priority, event_data))
        #         # Process the event
        #         # (For now, we just print it)
        #         time.sleep(1)  # Simulate event processing
        #     except queue.Empty:
        #         pass  # No event in the queue, continue waiting
        # print("Event thread shutdown.")

    def shutdown(self):
        self.shutdown_event.set()
        self.new_event_event.set()  # Wake up the thread in case it's waiting

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
                    event = self.event_list_thread.event_list.pop(0)
                    print("Event processed:", event)
            time.sleep(2)

class ActionUpdaterThread(threading.Thread):
    def __init__(self):
        super(ActionUpdaterThread, self).__init__()

    def run(self):
        while True:
            # Simulate updating actions
            print("Actions updated")
            time.sleep(3)

if __name__ == "__main__":
    # Create an instance of the EventListThread
    event_list_thread = EventListThread()

    # Create instances of StateMachineThread and ActionUpdaterThread
    state_machine_thread = StateMachineThread(event_list_thread)
    action_updater_thread = ActionUpdaterThread()

    # Start all threads
    event_list_thread.start()
    state_machine_thread.start()
    action_updater_thread.start()
    
    # Add events with different priorities
    event_list_thread.add_event(2, "Low priority event")
    event_list_thread.add_event(1, "High priority event")
    event_list_thread.add_event(3, "Medium priority event")

    # Wait for a while to let the events be processed
    time.sleep(5)

    # Shutdown the event thread
    event_list_thread.shutdown()
    event_list_thread.join()