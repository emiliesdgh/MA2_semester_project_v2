import ThymioStates
from ThymioStates import ThymioStates

from tdmclient import ClientAsync, aw

import numpy as np

import threading
import time
import queue

class EventListThread(threading.Thread):
    def __init__(self, robot):
        super(EventListThread, self).__init__()
        self.event_queue = queue.PriorityQueue()
        self.event_list = []
        self.event_list_lock = threading.Lock()  # Lock for protecting access to event list
        self.shutdown_event = threading.Event()  # Event to signal shutdown
        self.stop = True
        self.robot = robot

    def add_event(self, priority, event_data):
        self.event_queue.put((priority, event_data))

    def run(self):
        self.stop = False
        while not self.stop:
            # Read information from Thymio
            self.robot.update()
            print(self.robot.prox)
            # add event here
            self.add_event(0, "1st priority --> buttons")
            self.add_event(1, "2nd priority --> sensors")
            self.add_event(2, "3rd priority --> accelerometer")
            self.add_event(3, "4th priority --> microphone")
          
            #
            while not self.event_queue.empty():
                priority, event_data = self.event_queue.get()
                print("Event added with priority {}: {}".format(priority, event_data))

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

    def kill(self):
        self.stop = True


if __name__ == "__main__":

    from StateMachineThread import StateMachineThread, ActionUpdaterThread
    try:
        robot = ThymioStates()


        # Create an instance of the EventListThread
        event_list_thread = EventListThread(robot)

        # Create instances of StateMachineThread and ActionUpdaterThread
        state_machine_thread = StateMachineThread(event_list_thread)
        action_updater_thread = ActionUpdaterThread()

        # Start all threads
        event_list_thread.start()
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