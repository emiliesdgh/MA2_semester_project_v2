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
