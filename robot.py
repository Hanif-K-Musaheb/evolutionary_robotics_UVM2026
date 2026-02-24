from motor import MOTOR
import pyrosim.pyrosim as pyrosim
from sensor import SENSOR
import constants as c
import numpy as np
import pybullet as p


class ROBOT:
    def __init__(self):
        pass
        

    def Prepare_To_Sense(self):
        self.sensors={}
        for linkName in pyrosim.linkNamesToIndices:
            self.sensors[linkName] = SENSOR(linkName)

    def sense(self,i):
        for s in self.sensors:
            self.sensors[s].Get_Value(i)

    def Prepare_To_Act(self):
        self.motors={}
        for jointName in pyrosim.jointNamesToIndices:
            self.motors[jointName] = MOTOR(jointName)
    
    def Act(self,i,robotID):
        for m in self.motors:
            self.motors[m].set_value(i,robotID)



        
