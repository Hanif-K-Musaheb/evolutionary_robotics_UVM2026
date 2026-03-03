from motor import MOTOR
import pyrosim.pyrosim as pyrosim
from sensor import SENSOR
import constants as c
import numpy as np
import pybullet as p
from pyrosim.neuralNetwork import NEURAL_NETWORK

class ROBOT:
    def __init__(self):
        self.nn = NEURAL_NETWORK("brain.nndf")#adds the neural net to nndf file
        

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
    
    def Think(self):
        self.nn.Update()
        self.nn.Print()
        



        
