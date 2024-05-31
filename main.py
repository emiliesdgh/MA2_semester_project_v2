import ThymioStates
from ThymioStates import ThymioStates

from EventListThread import EventListThread

from buttonCenterThread import ButtonCenterThread
from buttonFrontThread import ButtonFrontThread
from buttonBackThread import ButtonBackThread
from buttonRightThread import ButtonRightThread
from buttonLeftThread import ButtonLeftThread

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
        
        # button_center_thread = ButtonCenterThread(event_list_thread, robot)
        # button_front_thread = ButtonFrontThread(event_list_thread, robot)
        # button_back_thread = ButtonBackThread(event_list_thread, robot)
        # button_right_thread = ButtonRightThread(event_list_thread, robot)
        # button_left_thread = ButtonLeftThread(event_list_thread, robot)
        # Create instances of StateMachineThread and ActionUpdaterThread
        # state_machine_thread = StateMachineThread(event_list_thread)
        # action_updater_thread = ActionUpdaterThread()

        # Start all threads
        event_list_thread.start()
        # state_machine_thread.start()

        program_list = [(robot.button_center, ButtonCenterThread),(robot.button_forward, ButtonFrontThread),(robot.button_backward, ButtonBackThread),(robot.button_left, ButtonLeftThread),(robot.button_right, ButtonRightThread)]
        # program_list = [(robot.button_center, button_center_thread),(robot.button_forward, button_front_thread),(robot.button_backward, button_back_thread),(robot.button_left, button_left_thread),(robot.button_right, button_right_thread)]
        
        program = None

        while True :

            if (robot.allButtons):

                print("dans le premier if")

                if (program is not None) and (robot.button_center) :

                    program.kill()
                    program = None
                    robot.setSpeedLeft(0)
                    robot.setSpeedRight(0)
                    robot.setLEDTop([32,32,32])

                if (program is None) and (robot.button_center):

                    print("dans le 2e if")
                    program = ButtonCenterThread(event_list_thread, robot)
                    print("avant le program start")
                    program.start()
                    print("apres le program start")

                elif (program is None) and (robot.button_forward):

                    print("dans le 2e if")
                    program = ButtonFrontThread(event_list_thread, robot)
                    print("avant le program start")
                    program.start()
                    print("apres le program start")

                elif (program is None) and (robot.button_backward):

                    print("dans le 2e if")
                    program = ButtonBackThread(event_list_thread, robot)
                    print("avant le program start")
                    program.start()
                    print("apres le program start")

                elif (program is None) and (robot.button_left):

                    print("dans le 2e if")
                    program = ButtonLeftThread(event_list_thread, robot)
                    print("avant le program start")
                    program.start()
                    print("apres le program start")

                elif (program is None) and (robot.button_right):

                    print("dans le 2e if")
                    program = ButtonRightThread(event_list_thread, robot)
                    print("avant le program start")
                    program.start()
                    print("apres le program start")
                    
            # for button_pressed, button_program in program_list:

            #     print("dans le for")
                
            #     if button_pressed:

            #         robot.setLEDTop([0,32,0])

            #         if button_pressed == robot.button_center :

            #             robot.setLEDTop([0,32,32])

            #             print("dans le 2e if")
            #             program = button_program(event_list_thread, robot)
            #             print("avant le program start")
            #             program.start()
            #             print("apres le program start")
                    
            #         elif button_pressed == robot.button_forward :

            #             print("dans le 2e if")
            #             program = button_program(event_list_thread, robot)
            #             print("avant le program start")
            #             program.start()
            #             print("apres le program start")
            
            # time.sleep(5)


            # # print("dans le while true")
            # if (robot.button_center):
            #     print("in Button center")
            #     button_center_thread.start()

            #     button_front_thread.kill()
            #     button_left_thread.kill()
            #     button_right_thread.kill()
            #     button_back_thread.kill()

            # elif (robot.button_forward):
            #     print("in Button Front")
            #     button_front_thread.start()

            #     button_center_thread.kill()
            #     button_left_thread.kill()
            #     button_right_thread.kill()
            #     button_back_thread.kill()
            
            # elif (robot.button_left):
            #     print("in Button Left")
            #     button_left_thread.start()

            #     button_center_thread.kill()
            #     button_front_thread.kill()
            #     button_right_thread.kill()
            #     button_back_thread.kill()

            # elif (robot.button_right):
            #     print("in Button Right")
            #     button_right_thread.start()

            #     button_center_thread.kill()
            #     button_front_thread.kill()
            #     button_left_thread.kill()
            #     button_back_thread.kill()

            # elif (robot.button_backward):
            #     print("in Button Back")
            #     button_back_thread.start()
                
            #     button_center_thread.kill()
            #     button_front_thread.kill()
            #     button_left_thread.kill()
            #     button_right_thread.kill()

            # Wait for a while to let the events be processed
            # time.sleep(20)

            # Shutdown the event thread
            # event_list_thread.kill()

        # action_updater_thread.kill()
    except Exception as e:
        print(e)
        event_list_thread.kill()
        # action_updater_thread.kill()