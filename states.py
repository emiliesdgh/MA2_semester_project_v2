import classes
from classes import Thymio

from tdmclient import ClientAsync, aw
# import matplotlib.pyplot as plt
import numpy as np

class ThymioStates :

    def __init__ (self) :

        self.button_center = 0
        self.button_forward = 0
        self.button_backward = 0
        self.button_right = 0
        self.button_left = 0

        self.client = ClientAsync()
        self.node = aw(self.client.wait_for_node())
        # aw(self.node.unlock())
        aw(self.node.lock())
        aw(self.node.wait_for_variables())

    def update(self):

        self.node = aw(self.client.wait_for_node())

        aw(self.node.wait_for_variables({"prox.horizontal"}))
        self.button_center = self.node.v.button.center
        self.button_forward = self.node.v.button.forward
        self.button_left = self.node.v.button.left
        self.button_right = self.node.v.button.right
        self.button_backward = self.node.v.button.backward
        # self.accelero = list(self.node.v.acc)
        # self.prox = list(self.node.v.prox.horizontal)
        self.prox = list(self.node["prox.horizontal"])
        # self.prox_ground = list(self.node.v.prox.ground)
        self.motor_left_speed = self.node["motor.left.speed"]
        self.motor_right_speed = self.node["motor.right.speed"]
        print("icii")

        # self.button_center = node.v.button.center
        # self.button_forward = node.v.button.forward
        # self.button_left = node.v.button.left
        # self.button_right = node.v.button.right
        # self.button_backward = node.v.button.backward
        # # self.accelero = list(self.node.v.acc)
        # # self.prox = list(self.node.v.prox.horizontal)
        # self.prox = list(node["prox.horizontal"])
        # # self.prox_ground = list(self.node.v.prox.ground)
        # self.motor_left_speed = node["motor.left.speed"]
        # self.motor_right_speed = node["motor.right.speed"]
        # print("icii")

       


    def getButtons(self):
        aw(self.node.wait_for_variables({"button.center"}))
        self.button_center = self.node.v.button.center

        aw(self.node.wait_for_variables({"button.forward"}))
        self.button_forward = self.node.v.button.forward

        aw(self.node.wait_for_variables({"button.left"}))
        self.button_left = self.node.v.button.left

        aw(self.node.wait_for_variables({"button.right"}))
        self.button_right = self.node.v.button.right

        aw(self.node.wait_for_variables({"button.backward"}))
        self.button_backward = self.node.v.button.backward

    def getAccelerometer(self):
        aw(self.node.wait_for_variables({"acc"}))
        self.accelero = list(self.node.v.acc)

    def getProxHorizontal(self):
        aw(self.node.wait_for_variables({"prox.horizontal"}))
        self.prox = list(self.node.v.prox.horizontal)
        print("la")
    
    def getProxGround(self):
        aw(self.node.wait_for_variables({"prox.ground"}))
        self.prox = list(self.node.v.prox.ground)

    def getSpeeds(self):
        aw(self.node.wait_for_variables({"motor.left.speed", "motor.right.speed"}))
        self.motor_left_speed = self.node["motor.left.speed"]
        self.motor_right_speed = self.node["motor.right.speed"]

    def __del__(self):
        aw(self.node.unlock())

    # def compareButtons(self):
    #     aw(self.node.wait_for_variables({"button.center"}))
    #     aw(self.node.wait_for_variables({"button.forward"}))
    #     aw(self.node.wait_for_variables({"button.left"}))
    #     aw(self.node.wait_for_variables({"button.right"}))
    #     aw(self.node.wait_for_variables({"button.backward"}))

    #     if (self.button_center == self.node.v.button.center) or (self.button_forward == self.node.v.button.forward) or (self.button_left == self.node.v.button.left)or(self.button_right == self.node.v.button.right)or(self.button_backward == self.node.v.button.backward):
    #         return True
    #     else: 
    #         return False


if __name__ == "__main__":
    
    # client = ClientAsync()
    # node = aw(client.wait_for_node())
    #     # aw(self.node.unlock())
    # aw(node.lock())
    # aw(node.wait_for_variables())

    robot = ThymioStates()
    while(True):
        # robot = ThymioStates()
        # node = aw(client.wait_for_node())

        # aw(node.wait_for_variables())

        # robot.getProxHorizontal()
        robot.update()
        print(robot.prox)
        print(robot.button_center)