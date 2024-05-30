from tdmclient import ClientAsync, aw

import numpy as np


import classes
from classes import Thymio

client = ClientAsync()
node = aw(client.wait_for_node())

aw(node.lock())
aw(node.wait_for_variables())

def accelerometer_effect(Thymio, node, motor_speed=100) :
    accel = list(node["acc"]) + [0]

    # print(accel[0]) 
    # max droite  : -18 - -20
    # max gauche : 22 - 25
    # max devant derrière : rien
    # ~2-3 quand a plat, augmente + quand penché côté senseur 6, 
    # augmente - quand penché côté senseur 5, change pas quand penché avant arrière

    # print(accel[1])
    # max gauche  droite :  rien
    # max devant : - 21 - -22
    # max derrière : 20 - 22
    #  ~-1,0,1 quand horizontal, change pas quand penché droite, gauche
    # augment + quand penché en arrière, augmente - quand penché en avant

    # print(accel[2])
    # max droite : -1 - 1
    # max gauche : 0 - 1
    # max devant : 0 - 1
    # max derrière : -2 - 0
    # ~-20,-21 quand horizontal sur le dos, diminue - quand placé sur les côtés


    # GAUCHE
    if accel[0] > 4: #Thymio is blue when placed on one of its sides
        Thymio.setLEDTop(node, [0,0,32])
        # on the side
        Thymio.setSpeedLeft(0, node)
        Thymio.setSpeedRight(motor_speed, node)

    # DROITE
    if accel[0]< -2: #Thymio is blue when placed on one of its sides
        Thymio.setLEDTop(node, [0,0,32])
        # on the side
        Thymio.setSpeedLeft(motor_speed, node)
        Thymio.setSpeedRight(0, node)

    # DERRIERE
    if accel[1] > 2: #Thymio is red when placed on its front or backside
        Thymio.setLEDTop(node, [32,0,0])
        # on back
        Thymio.setSpeedLeft(-motor_speed, node)
        Thymio.setSpeedRight(-motor_speed, node)

    # DEVANT
    if accel[1]< -2: #Thymio is red when placed on its front or backside
        Thymio.setLEDTop(node, [32,0,0])
        # on front
        Thymio.setSpeedLeft(motor_speed, node)
        Thymio.setSpeedRight(motor_speed, node)

    if accel[2] > 18 or accel[2] < -18: #Thymio is green when placed on its wheels or upside-down
        Thymio.setLEDTop(node, [0,32,0])
        # horizontal
        Thymio.setSpeedLeft(0, node)
        Thymio.setSpeedRight(0, node)


while(1) :

    accelerometer_effect(Thymio, node, motor_speed=50)