from motor import MOTOR
import pyrosim.pyrosim as pyrosim
from sensor import SENSOR
import constants as c
import numpy as np
import pybullet as p
from pyrosim.neuralNetwork import NEURAL_NETWORK
import os

class ROBOT:
    def __init__(self,solutionID):
        self.nn = NEURAL_NETWORK(f"brain_{solutionID}.nndf")#adds the neural net to nndf file
        self.solutionID = solutionID
       #os.system(f"rm brain_{solutionID}.nndf")
        
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
        for neuronName in self.nn.Get_Neuron_Names():
            if self.nn.Is_Motor_Neuron(neuronName):
                jointName = self.nn.Get_Motor_Neurons_Joint(neuronName)
                jointNameBytes = jointName.encode()
                desiredAngle = self.nn.Get_Value_Of(neuronName)
                self.motors[jointNameBytes].set_value(desiredAngle, robotID)



        # for m in self.motors:
        #     self.motors[m].set_value(i,robotID)

    def Get_Fitness(self,robotId):
        stateOfLinkZero = p.getLinkState(robotId,0)[0]
        xCoordinateOfLinkZero = stateOfLinkZero[0]
        #print(stateOfLinkZero,xCoordinateOfLinkZero)
        with open(f"tmp{self.solutionID}.txt", "w") as file:
            file.write(f"{xCoordinateOfLinkZero}")
        
        os.system(f"mv tmp{self.solutionID}.txt fitness{self.solutionID}.txt")
        #exit()



    
    def Think(self):
        self.nn.Update()
        self.nn.Print()
        



        
