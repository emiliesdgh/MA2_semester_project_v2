# test pour les threads

import classes
from classes import Thymio

from tdmclient import ClientAsync, aw

import numpy as np
import logging
import threading
import time

def acc():
    global acc, leds_top
    if acc[0]>18 or acc[0]<-18: #Thymio is blue when placed on one of its sides
        leds_top=[0,0,32]
    if acc[1]>18 or acc[1]<-18: #Thymio is red when placed on its front or backside
        leds_top=[32,0,0]
    if acc[2]>18 or acc[2]<-18: #Thymio is green when placed on its wheels or upside-down
        leds_top=[0,32,0]

def accelerometer_effect(Thymio, node, motor_speed=50) :
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
    if accel[0]>0: #Thymio is blue when placed on one of its sides
        Thymio.setLEDTop(node, [0,0,32])
        # on the side
        Thymio.setSpeedLeft((22-accel[0])*motor_speed, node)
        Thymio.setSpeedRight((22-accel[0])*motor_speed, node)

    # DROITE
    if accel[0]< 0: #Thymio is blue when placed on one of its sides
        Thymio.setLEDTop(node, [0,0,32])
        # on the side
        Thymio.setSpeedLeft((accel[0]-22)*motor_speed, node)
        Thymio.setSpeedRight((accel[0]-22)*motor_speed, node)

    # DERRIERE
    if accel[1]>0: #Thymio is red when placed on its front or backside
        Thymio.setLEDTop(node, [32,0,0])
        # on back
        Thymio.setSpeedLeft((22-accel[1])*motor_speed, node)
        Thymio.setSpeedRight((22-accel[1])*motor_speed, node)

    # DEVANT
    if accel[1]< 0: #Thymio is red when placed on its front or backside
        Thymio.setLEDTop(node, [32,0,0])
        # on front
        Thymio.setSpeedLeft((accel[1]-22)*motor_speed, node)
        Thymio.setSpeedRight((accel[1]-22)*motor_speed, node)

    if accel[2]>18 or accel[2]<-18: #Thymio is green when placed on its wheels or upside-down
        Thymio.setLEDTop(node, [0,32,0])
        # horizontal
        Thymio.setSpeedLeft(0, node)
        Thymio.setSpeedRight(0, node)