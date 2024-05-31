# from tdmclient import ClientAsync, aw
from tdmclient import ClientAsync, aw
import asyncio
import matplotlib.pyplot as plt
import numpy as np
import copy

import logging
import threading
import time

#import the classes from the other modules
from classes import Thymio

import W4_T1_PS_24_03_07
import W6_T1_PS_24_03_30
import W8_T1_PS_24_04_19
import W8_T1_PS_24_04_22
import W6_T1_PS_24_04_03

import fonctions

client = ClientAsync()
node = aw(client.wait_for_node())
# aw(node.unlock())
aw(node.lock())
aw(node.wait_for_variables())



# aw(node.register_events([("StopnUnlock", )]))

# program = """
# onevent StopnUnlock

#     fonctions.setButtons(robot, 0)

#     print(robot.button_center)
#     fonctions.stop_program(robot, node, motor_speed=0)
#     aw(node.unlock())
# """


# # The event data are obtained from variable event.args:
# program = """
# onevent StopnUnlock
#     motor.left.target = event.args[0]
#     motor.right.target = event.args[1]
# """
# aw(node.compile(program))
# aw(node.run())


#Classes initialization
robot = Thymio()

def update_sensors_data(robot, node):

    # get button values
    robot.getProxHorizontal(node)
    robot.getButtons(node)

# def thread_buttonCenter(name) :

#     logging.info("Thread %s: starting", name)
#     time.sleep(2)

#     # aw(node.send_events({"StopnUnlock": }))

#     logging.info("Thread %s: finishing", name)

# def thread_buttonCenter(event) :

#     if (robot.button_center) :
#         # robot.buttonForward = 0
#         W6_T1_PS_24_03_30.setButtons(robot, 0)

#         print(robot.button_center)
#         W6_T1_PS_24_03_30.stop_program(robot, node, motor_speed=0)
#         aw(node.unlock())
        # break


# def main() :

    # INTHREAD = threading.Event()

    # threadToStop = threading.Thread(target=thread_buttonCenter, args=(INTHREAD,))

    # threadToStop.start()



while(1) :

    # aw(client.sleep(0.1))
    update_sensors_data(robot, node)

    robot.setLEDTop(node, [32,32,32])

    # W8_T1_PS_24_04_19.accelerometer_effect(robot, node)
    # fonctions.accelerometer_effect(robot, node)

    fonctions.microphone(robot,node,client,motor_speed=50)

    # format = "%(asctime)s: %(message)s"
    # logging.basicConfig(format=format, level=logging.INFO,
    #                     datefmt="%H:%M:%S")

    # logging.info("Main    : before creating thread")
    # x = threading.Thread(target=thread_buttonCenter, args=(1,))
    # logging.info("Main    : before running thread")
    # x.start()
    # logging.info("Main    : wait for the thread to finish")
    # # x.join()
    # logging.info("Main    : all done")

    # W6_T1_PS_24_04_02.acc()

########

    if (robot.button_center) :

        # robot.buttonForward = 0
        fonctions.setButtons(robot, 0)

        print(robot.button_center)
        fonctions.stop_program(robot, node, motor_speed=0)
        aw(node.unlock())
        break

    proxG = list(node["prox.ground.ambiant"]) + [0]

    # print(proxG[0])
    # print(proxG[1])

    

######## MODIFIED COSTUME

    prox = list(node["prox.horizontal"]) + [0]

    # if(prox[2]) :
    #     update_sensors_data(robot, node)
    #     print(prox[2])

    #     fonctions.see_costume(robot, node, motor_speed=50)
    # else :
    #     fonctions.no_costume(robot, node, motor_speed=0)
    #     print(prox[2])

######## 05.04.2024

    # print(prox[5])
    # print(prox[6])

    # if (prox[5]>1000 and prox[6]>1000 and proxG[0]>10) :
    
    # fonctions.programBack(robot, node, client)
    

# ######## DOUBLED COSTUME

    # if ((prox[5]>1000 and prox[6]<1000) or (prox[5]<1000 and prox[6]>1000)) :

    # fonctions.ext_interaction(robot, node, motor_speed=100, obs_threshold=500)

    # if (robot.button_forward and not(robot.buttonForward)) :

    #     fonctions.setButtons(robot, 0)

    #     robot.buttonForward = 1


    # elif (robot.button_forward and robot.buttonForward) :

    #     robot.buttonForward = 0
    #     robot.setLEDTop(node, [0,0,32])
    #     aw(client.sleep(2))


    # if (robot.buttonForward) :

    #     # while (not robot.button_center) :

    #     fonctions.programFront(robot, node, client)

########

    # if (robot.button_backward) :

    #     fonctions.setButtons(robot, 0)

    #     robot.buttonBackward = 1

    # if (robot.buttonBackward) :

    #     fonctions.programBack(robot, node, client)

# INTHREAD.set()
# threadToStop.join()


# if __name__ == "__main__":
#         main()


# import classes
# from classes import thymio

###############################################################

# # # ALL FUNCTIONS

# # # import ThymioStates
# # # from ThymioStates import ThymioStates

# # # from tdmclient import ClientAsync, aw
# # # import numpy as np

# # # # thymio = ThymioStates()

# # # def setButtons(Thymio, value) :

# # #         Thymio.buttonForward = value
# # #         Thymio.buttonBackward = value
# # #         Thymio.buttonCenter = value
# # #         Thymio.buttonRight = value
# # #         Thymio.buttonLeft = value


# # # def stop_program(Thymio) :

# # #     Thymio.setLEDTop([32,32,32])

# # #     Thymio.setSpeedLeft(0)
# # #     Thymio.setSpeedRight(0)

# # # def microphone(Thymio, client, motor_speed=50) :
# # #     # mic = node.v.mic.intensity

# # #     print(Thymio.mic)
# # #     if Thymio.microphone_set and Thymio.mic>20 :
# # #         Thymio.setSpeedLeft(-motor_speed)
# # #         Thymio.setSpeedRight(motor_speed)

# # #         aw(client.sleep(2))

# # #         Thymio.setSpeedLeft(0)
# # #         Thymio.setSpeedRight(0)

# # #         Thymio.microphone_set = 0

# # #     elif (not Thymio.microphone_set) and Thymio.mic>20 :
# # #         Thymio.setSpeedLeft(motor_speed)
# # #         Thymio.setSpeedRight(-motor_speed)

# # #         aw(client.sleep(2))

# # #         Thymio.setSpeedLeft(0)
# # #         Thymio.setSpeedRight(0)

# # #         Thymio.microphone_set = 1

# # # def accelerometer_effect(Thymio, motor_speed=100) :
# # #     # accel = list(node["acc"]) + [0]

# # #     # print(accel[0]) 
# # #     # max droite  : -18 - -20
# # #     # max gauche : 22 - 25
# # #     # max devant derrière : rien
# # #     # ~2-3 quand a plat, augmente + quand penché côté senseur 6, 
# # #     # augmente - quand penché côté senseur 5, change pas quand penché avant arrière

# # #     # print(accel[1])
# # #     # max gauche  droite :  rien
# # #     # max devant : - 21 - -22
# # #     # max derrière : 20 - 22
# # #     #  ~-1,0,1 quand horizontal, change pas quand penché droite, gauche
# # #     # augment + quand penché en arrière, augmente - quand penché en avant

# # #     # print(accel[2])
# # #     # max droite : -1 - 1
# # #     # max gauche : 0 - 1
# # #     # max devant : 0 - 1
# # #     # max derrière : -2 - 0
# # #     # ~-20,-21 quand horizontal sur le dos, diminue - quand placé sur les côtés


# # #     # GAUCHE
# # #     if Thymio.accel[0] > 4: #Thymio is blue when placed on one of its sides
# # #         Thymio.setLEDTop([0,0,32])
# # #         # on the side
# # #         Thymio.setSpeedLeft(0)
# # #         Thymio.setSpeedRight(motor_speed)

# # #     # DROITE
# # #     if Thymio.accel[0]< -2: #Thymio is blue when placed on one of its sides
# # #         Thymio.setLEDTop([0,0,32])
# # #         # on the side
# # #         Thymio.setSpeedLeft(motor_speed)
# # #         Thymio.setSpeedRight(0)

# # #     # DERRIERE
# # #     if Thymio.accel[1] > 2: #Thymio is red when placed on its front or backside
# # #         Thymio.setLEDTop([32,0,0])
# # #         # on back
# # #         Thymio.setSpeedLeft(-motor_speed)
# # #         Thymio.setSpeedRight(-motor_speed)

# # #     # DEVANT
# # #     if Thymio.accel[1]< -2: #Thymio is red when placed on its front or backside
# # #         Thymio.setLEDTop([32,0,0])
# # #         # on front
# # #         Thymio.setSpeedLeft(motor_speed)
# # #         Thymio.setSpeedRight(motor_speed)

# # #     if Thymio.accel[2] > 18 or Thymio.accel[2] < -18: #Thymio is green when placed on its wheels or upside-down
# # #         Thymio.setLEDTop([0,32,0])
# # #         # horizontal
# # #         Thymio.setSpeedLeft(0)
# # #         Thymio.setSpeedRight(0)

# # # def see_costume(Thymio, motor_speed=0) :

# # #     Thymio.setSpeedLeft(motor_speed)
# # #     Thymio.setSpeedRight(motor_speed)

# # # def no_costume(Thymio, motor_speed=0) :

# # #     Thymio.setLEDTop([0,32,0])

# # #     Thymio.setSpeedLeft(motor_speed)
# # #     Thymio.setSpeedRight(motor_speed)


# # # def ext_interaction(Thymio, motor_speed=100) :

# # #     # prox = list(node["prox.horizontal"]) + [0]

# # #     if (Thymio.prox[5] + Thymio.prox[6] < 6000) :

# # #         if Thymio.prox[5] > Thymio.prox[6] :

# # #             # color = [24,24,24,0,0,0,0,24]
# # #             # Thymio.setLEDCircle(color)

# # #             Thymio.setSpeedLeft(motor_speed)
# # #             Thymio.setSpeedRight(-motor_speed)

# # #         elif Thymio.prox[6] > Thymio.prox[5] : # Thymio needs to contourn the obstacle counterclockwise
# # #             # color = [24,24,0,0,0,0,24,24]
# # #             # Thymio.setLEDCircle(color)

# # #             Thymio.setSpeedLeft(-motor_speed)
# # #             Thymio.setSpeedRight(motor_speed)

# # #         elif Thymio.prox[0]+Thymio.prox[1] > Thymio.prox[3] + Thymio.prox[4] :

# # #             # color = [0,24,24,24,24,0,0,0]
# # #             # Thymio.setLEDCircle(color)

# # #             Thymio.setSpeedLeft(-motor_speed)
# # #             Thymio.setSpeedRight(motor_speed)

# # #         elif Thymio.prox[0]+Thymio.prox[1] < Thymio.prox[3] + Thymio.prox[4] :

# # #             # color = [0,0,0,0,24,24,24,24]
# # #             # Thymio.setLEDCircle(color)

# # #             Thymio.setSpeedLeft(motor_speed)
# # #             Thymio.setSpeedRight(-motor_speed)

# # #         elif Thymio.prox[2] > (Thymio.prox[0] or Thymio.prox[1] or Thymio.prox[3] or Thymio.prox[4]) :

# # #             # color = [0,0,0,24,24,24,0,0]
# # #             # Thymio.setLEDCircle(color)

# # #             Thymio.setSpeedLeft(-motor_speed)
# # #             Thymio.setSpeedRight(-motor_speed)

# # #         else :
# # #             # color = [0,0,0,0,0,0,0,0]
# # #             # Thymio.setLEDCircle(color)

# # #             Thymio.setSpeedLeft(0)
# # #             Thymio.setSpeedRight(0)


# # # def programFront (Thymio, client) :

# # #     Thymio.setLEDTop([20,0,32])
# # #     color = [0,0,0,0,0,0,0,0]
# # #     Thymio.setLEDCircle(color)

# # #     Thymio.setSpeedLeft(50)
# # #     Thymio.setSpeedRight(-50)

# # #     aw(client.sleep(2))

# # #     Thymio.setSpeedLeft(-50)
# # #     Thymio.setSpeedRight(50)

# # #     aw(client.sleep(2))
    

# # # def programBack (Thymio) :

# # #     # prox = list(node["prox.horizontal"]) + [0]
# # #     # proxG = list(node["prox.ground.ambiant"]) + [0]

# # #     if (Thymio.prox[5]>1000 and Thymio.prox[6]>1000 and Thymio.prox_ground[0]>10) :

# # #         Thymio.setLEDTop([20,0,32])
# # #         color = [0,0,0,0,0,0,0,0]
# # #         Thymio.setLEDCircle(color)

# # #         Thymio.setSpeedLeft(50)
# # #         Thymio.setSpeedRight(50)
