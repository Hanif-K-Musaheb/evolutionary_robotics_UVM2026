from motor import MOTOR
import pyrosim.pyrosim as pyrosim
from sensor import SENSOR
import constants as c
import numpy as np
import pybullet as p
from pyrosim.neuralNetwork import NEURAL_NETWORK
import os
import time
import csv


class ROBOT:
    def __init__(self,solutionID):
        self.nn = NEURAL_NETWORK(f"brain_{solutionID}.nndf")#adds the neural net to nndf file
        self.solutionID = solutionID
        #os.system(f"rm brain_{solutionID}.nndf")
        self.fitness_data=[]
        
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
                self.motors[jointNameBytes].set_value(desiredAngle*c.motorJointRange, robotID)

    def log_sense(self,it):
        self.nn.save_hidden_neuron_data(it)
        self.nn.save_recurrent_neuron_data(it)
        

        # for m in self.motors:
        #     self.motors[m].set_value(i,robotID)
    
    def collect_fitness_data(self,solutionID):
        basePositionAndOrientation = p.getBasePositionAndOrientation(1)
        basePosition = basePositionAndOrientation[0]
        xPosition = basePosition[0]

        self.fitness_data.append(xPosition)

    
    
    def log_fittness(self,solutionID):
        labelled_data = [solutionID, *self.fitness_data]
        with open('normal_brain_generation_fitness.csv', 'a', newline='') as file:#'peak_brainacs_fitness_data.csv'
            writer = csv.writer(file)
            writer.writerow(labelled_data)
        

    def Get_Fitness(self,robotId):
        basePositionAndOrientation = p.getBasePositionAndOrientation(robotId)
        basePosition = basePositionAndOrientation[0]
        xPosition = basePosition[0]

        #print(stateOfLinkZero,xCoordinateOfLinkZero)
        with open(f"tmp{self.solutionID}.txt", "w") as file:
            file.write(f"{xPosition}")
        
        os.system(f"mv tmp{self.solutionID}.txt fitness{self.solutionID}.txt")
        #exit()



    
    def Think(self):
        self.nn.Update()
        self.nn.Print()
        



        
