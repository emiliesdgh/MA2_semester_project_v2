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
        
        button_center_thread = ButtonCenterThread(event_list_thread, robot)
        button_front_thread = ButtonFrontThread(event_list_thread, robot)
        button_back_thread = ButtonBackThread(event_list_thread, robot)
        button_right_thread = ButtonRightThread(event_list_thread, robot)
        button_left_thread = ButtonLeftThread(event_list_thread, robot)
        # Create instances of StateMachineThread and ActionUpdaterThread
        # state_machine_thread = StateMachineThread(event_list_thread)
        # action_updater_thread = ActionUpdaterThread()

        # Start all threads
        event_list_thread.start()
        # state_machine_thread.start()
        
        while True :

            # print("dans le while true")
            if (robot.button_center):
                print("in Button center")
                button_center_thread.start()

                button_front_thread.kill()
                button_left_thread.kill()
                button_right_thread.kill()
                button_back_thread.kill()

            elif (robot.button_forward):
                print("in Button Front")
                button_front_thread.start()

                button_center_thread.kill()
                button_left_thread.kill()
                button_right_thread.kill()
                button_back_thread.kill()
            
            elif (robot.button_left):
                print("in Button Left")
                button_left_thread.start()

                button_center_thread.kill()
                button_front_thread.kill()
                button_right_thread.kill()
                button_back_thread.kill()

            elif (robot.button_right):
                print("in Button Right")
                button_right_thread.start()

                button_center_thread.kill()
                button_front_thread.kill()
                button_left_thread.kill()
                button_back_thread.kill()

            elif (robot.button_backward):
                print("in Button Back")
                button_back_thread.start()
                
                button_center_thread.kill()
                button_front_thread.kill()
                button_left_thread.kill()
                button_right_thread.kill()

            # Wait for a while to let the events be processed
            # time.sleep(20)

            # Shutdown the event thread
            # event_list_thread.kill()

        # action_updater_thread.kill()
    except Exception as e:
        print(e)
        event_list_thread.kill()
        # action_updater_thread.kill()