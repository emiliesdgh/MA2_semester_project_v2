import classes
from classes import Thymio

from tdmclient import ClientAsync, aw
import numpy as np


def setButtons(Thymio, value) :

        Thymio.buttonCenter = value
        Thymio.buttonForward = value
        Thymio.buttonBackward = value
        Thymio.buttonRight = value
        Thymio.buttonLeft = value


def stop_program(Thymio, motor_speed=0) :

    Thymio.setLEDTop([32,32,32])

    Thymio.setSpeedLeft(motor_speed)
    Thymio.setSpeedRight(motor_speed)

def microphone(Thymio, node, client, motor_speed=50) :
    mic = node.v.mic.intensity

    print(mic)
    if Thymio.microphone_set and mic>20 :
        Thymio.setSpeedLeft(-motor_speed, node)
        Thymio.setSpeedRight(motor_speed, node)

        aw(client.sleep(2))

        Thymio.setSpeedLeft(0, node)
        Thymio.setSpeedRight(0, node)

        Thymio.microphone_set = 0

    elif (not Thymio.microphone_set) and mic>20 :
        Thymio.setSpeedLeft(motor_speed, node)
        Thymio.setSpeedRight(-motor_speed, node)

        aw(client.sleep(2))

        Thymio.setSpeedLeft(0, node)
        Thymio.setSpeedRight(0, node)

        Thymio.microphone_set = 1
        




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

def see_costume(Thymio, motor_speed=0) :

    print("dans fonction see_costume")

    # Thymio.setLEDTop([0,32,0])

    Thymio.setSpeedLeft(motor_speed)
    Thymio.setSpeedRight(motor_speed)

def no_costume(Thymio, motor_speed=0) :

    Thymio.setLEDTop([0,32,0])

    Thymio.setSpeedLeft(motor_speed)
    Thymio.setSpeedRight(motor_speed)


def ext_interaction(Thymio, node, motor_speed=100) :

    prox = list(node["prox.horizontal"]) + [0]

    if (prox[5] + prox[6] < 6000) :

        if prox[5] > prox[6] :

            color = [24,24,24,0,0,0,0,24]
            Thymio.setLEDCircle(node, color)

            Thymio.setSpeedLeft(motor_speed, node)
            Thymio.setSpeedRight(-motor_speed, node)

        elif prox[6] > prox[5] : # Thymio needs to contourn the obstacle counterclockwise
            color = [24,24,0,0,0,0,24,24]
            Thymio.setLEDCircle(node, color)

            Thymio.setSpeedLeft(-motor_speed, node)
            Thymio.setSpeedRight(motor_speed, node)

        elif prox[0]+prox[1] > prox[3] + prox[4] :

            color = [0,24,24,24,24,0,0,0]
            Thymio.setLEDCircle(node, color)

            Thymio.setSpeedLeft(-motor_speed, node)
            Thymio.setSpeedRight(motor_speed, node)

        elif prox[0]+prox[1] < prox[3] + prox[4] :

            color = [0,0,0,0,24,24,24,24]
            Thymio.setLEDCircle(node, color)

            Thymio.setSpeedLeft(motor_speed, node)
            Thymio.setSpeedRight(-motor_speed, node)

        elif prox[2] > (prox[0] or prox[1] or prox[3] or prox[4]) :

            color = [0,0,0,24,24,24,0,0]
            Thymio.setLEDCircle(node, color)

            Thymio.setSpeedLeft(-motor_speed, node)
            Thymio.setSpeedRight(-motor_speed, node)

        else :
            color = [0,0,0,0,0,0,0,0]
            Thymio.setLEDCircle(node, color)

            Thymio.setSpeedLeft(0, node)
            Thymio.setSpeedRight(0, node)


def programFront (Thymio, node, client) :

    Thymio.setLEDTop(node, [20,0,32])
    color = [0,0,0,0,0,0,0,0]
    Thymio.setLEDCircle(node, color)

    Thymio.setSpeedLeft(50, node)
    Thymio.setSpeedRight(-50, node)

    aw(client.sleep(2))

    Thymio.setSpeedLeft(-50, node)
    Thymio.setSpeedRight(50, node)

    aw(client.sleep(2))
    

def programBack (Thymio, node, client) :

    prox = list(node["prox.horizontal"]) + [0]
    proxG = list(node["prox.ground.ambiant"]) + [0]

    if (prox[5]>1000 and prox[6]>1000 and proxG[0]>10) :

        Thymio.setLEDTop(node, [20,0,32])
        color = [0,0,0,0,0,0,0,0]
        Thymio.setLEDCircle(node, color)

        Thymio.setSpeedLeft(50, node)
        Thymio.setSpeedRight(50, node)
