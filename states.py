import classes
from classes import Thymio

from tdmclient import ClientAsync, aw
# import matplotlib.pyplot as plt
import numpy as np

class ThymioStates :

    def getButtons(self, node):
        aw(node.wait_for_variables({"button.center"}))
        self.button_center = node.v.button.center

        aw(node.wait_for_variables({"button.forward"}))
        self.button_forward = node.v.button.forward

        aw(node.wait_for_variables({"button.left"}))
        self.button_left = node.v.button.left

        aw(node.wait_for_variables({"button.right"}))
        self.button_right = node.v.button.right

        aw(node.wait_for_variables({"button.backward"}))
        self.button_backward = node.v.button.backward

    # def compareButtons(self, node):
    #     aw(node.wait_for_variables({"button.center"}))
    #     aw(node.wait_for_variables({"button.forward"}))
    #     aw(node.wait_for_variables({"button.left"}))
    #     aw(node.wait_for_variables({"button.right"}))
    #     aw(node.wait_for_variables({"button.backward"}))

    #     if (self.button_center == node.v.button.center) or (self.button_forward == node.v.button.forward) or (self.button_left == node.v.button.left)or(self.button_right == node.v.button.right)or(self.button_backward == node.v.button.backward):
    #         return True
    #     else: 
    #         return False