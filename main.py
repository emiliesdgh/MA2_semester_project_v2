import ThymioStates
from ThymioStates import ThymioStates

from EventListThread import EventListThread

from ButtonCenterThread import ButtonCenterThread
from ButtonFrontThread import ButtonFrontThread
from ButtonBackThread import ButtonBackThread
from ButtonRightThread import ButtonRightThread
from ButtonLeftThread import ButtonLeftThread

from tdmclient import ClientAsync, aw

import numpy as np

import fonctions

import threading
import time
import queue

import fonctions

client = ClientAsync()
node = aw(client.wait_for_node())
# # aw(node.unlock())
# aw(node.lock())
aw(node.wait_for_variables())

if __name__ == "__main__":
    try:
        robot = ThymioStates()


        # Create an instance of the EventListThread
        event_list_thread = EventListThread(robot)

        button_front_thread = ButtonFrontThread(event_list_thread)
        button_center_thread = ButtonCenterThread(event_list_thread)
        button_back_thread = ButtonBackThread(event_list_thread)
        button_right_thread = ButtonRightThread(event_list_thread)
        button_left_thread = ButtonLeftThread(event_list_thread)
        # Create instances of StateMachineThread and ActionUpdaterThread
        # state_machine_thread = StateMachineThread(event_list_thread)
        # action_updater_thread = ActionUpdaterThread()

        # Start all threads
        event_list_thread.start()
        # state_machine_thread.start()
        # action_updater_thread.start()
        
        # # Add events with different priorities
        # event_list_thread.add_event(2, "Low priority event")
        # event_list_thread.add_event(1, "High priority event")
        # event_list_thread.add_event(3, "Medium priority event")
        while True :

            if (robot.button_center):
                print(robot.button_center)
                button_center_thread.start()
                # button_front_thread.stop()
                # button_left_thread.stop()
                # button_right_thread.stop()
                # button_back_thread.stop()

            elif (robot.button_forward):
                print("in Button Front")
                button_front_thread.start()
                # button_center_thread.stop()
                # button_left_thread.stop()
                # button_right_thread.stop()
                # button_back_thread.stop()
            
            elif (robot.button_left):
                print("in Button Left")
                button_left_thread.start()
                # button_center_thread.stop()
                # button_front_thread.stop()
                # button_right_thread.stop()
                # button_back_thread.stop()

            elif (robot.button_right):
                print("in Button Right")
                button_right_thread.start()
                # button_center_thread.stop()
                # button_front_thread.stop()
                # button_left_thread.stop()
                # button_back_thread.stop()

            elif (robot.button_backward):
                print("in Button Back")
                button_back_thread.start()
                # button_center_thread.stop()
                # button_front_thread.stop()
                # button_left_thread.stop()
                # button_right_thread.stop()

            # Wait for a while to let the events be processed
            time.sleep(20)

            # Shutdown the event thread
            event_list_thread.kill()
        # action_updater_thread.kill()
    except Exception as e:
        print(e)
        event_list_thread.kill()
        # action_updater_thread.kill()