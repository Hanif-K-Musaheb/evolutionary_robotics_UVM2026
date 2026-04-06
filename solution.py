import numpy as np
import pyrosim.pyrosim as pyrosim
import os
import random
import time
import constants as c

length = 1
width = 1
height = 1

class SOLUTION:
    def __init__(self,nextAvailableID):
        self.myID = nextAvailableID
        self.weights = (np.random.rand(c.numSensorNeurons,c.numMotorNeurons))*2-1
    

    def Start_Simulation(self,directOrGUI):
        #if self.myID == 0:
        self.Create_World()
        self.Create_Body()
        self.Create_Brain()

        

        if os.path.exists(f"fitness{self.myID}.txt"):
            os.remove(f"fitness{self.myID}.txt")
            
        os.system(f"python3 simulate.py {directOrGUI} {self.myID} 2>&1 &")


    def Wait_For_Simulation_To_End(self):
        while not os.path.exists(f"fitness{self.myID}.txt"):
            time.sleep(0.01)

        fitness_file = open(f"fitness{self.myID}.txt")
        self.fitness = float(fitness_file.readline())
        print(f"\nfitness {self.myID}:{self.fitness}")
        fitness_file.close()
        os.system(f"rm fitness{self.myID}.txt")
        os.system(f"rm world_{self.myID}.sdf")
        os.system(f"rm body_{self.myID}.urdf")



    def Mutate(self):
        randomRow = random.randint(0, c.numSensorNeurons - 1)
        randomColumn = random.randint(0, c.numMotorNeurons - 1)
        self.weights[randomRow][randomColumn] = random.random() * 2 - 1 

    def Set_ID(self, nextAvailableID):
        self.myID = nextAvailableID
        






    
    def Create_World(self):
        pyrosim.Start_SDF(f"world_{self.myID}.sdf")
        pyrosim.End()
    
    def Create_Body(self):
        pyrosim.Start_URDF(f"body_{self.myID}.urdf")
        pyrosim.Send_Cube(name="Torso", pos=[0, 0, 1], size=[length, width, height])

        pyrosim.Send_Joint(name="Torso_BackLeg", parent="Torso", child="BackLeg", type="revolute", position=[0, -0.5, 1], jointAxis= "1 0 0")
        pyrosim.Send_Cube(name="BackLeg", pos=[0, -0.5, 0], size=[0.2, 1, 0.2])

        pyrosim.Send_Joint(name="Torso_FrontLeg", parent="Torso", child="FrontLeg", type="revolute", position=[0, 0.5, 1], jointAxis= "1 0 0")
        pyrosim.Send_Cube(name="FrontLeg", pos=[0, 0.5, 0], size=[0.2, 1, 0.2])

        pyrosim.Send_Joint(name="Torso_LeftLeg", parent="Torso", child="LeftLeg", type="revolute", position=[-0.5, 0, 1], jointAxis= "0 1 0")
        pyrosim.Send_Cube(name="LeftLeg", pos=[-0.5, 0, 0], size=[1, 0.2, 0.2])

        pyrosim.Send_Joint(name="Torso_RightLeg", parent="Torso", child="RightLeg", type="revolute", position=[0.5, 0, 1], jointAxis= "0 1 0")
        pyrosim.Send_Cube(name="RightLeg", pos=[0.5, 0, 0], size=[1, 0.2, 0.2])

        pyrosim.Send_Joint(name="BackLeg_BackLowerLeg", parent="BackLeg", child="BackLowerLeg", type="revolute", position=[0, -1, 0], jointAxis= "1 0 0")
        pyrosim.Send_Cube(name="BackLowerLeg", pos=[0, 0, -0.5], size=[0.2, 0.2, 1])

        pyrosim.Send_Joint(name="FrontLeg_FrontLowerLeg", parent="FrontLeg", child="FrontLowerLeg", type="revolute", position=[0, 1, 0], jointAxis= "1 0 0")
        pyrosim.Send_Cube(name="FrontLowerLeg", pos=[0, 0, -0.5], size=[0.2, 0.2, 1])

        pyrosim.Send_Joint(name="LeftLeg_LeftLowerLeg", parent="LeftLeg", child="LeftLowerLeg", type="revolute", position=[-1, 0, 0], jointAxis= "0 1 0")
        pyrosim.Send_Cube(name="LeftLowerLeg", pos=[0, 0, -0.5], size=[0.2, 0.2, 1])

        pyrosim.Send_Joint(name="RightLeg_RightLowerLeg", parent="RightLeg", child="RightLowerLeg", type="revolute", position=[1, 0, 0], jointAxis= "0 1 0")
        pyrosim.Send_Cube(name="RightLowerLeg", pos=[0, 0, -0.5], size=[0.2, 0.2, 1])

        pyrosim.End()



    def Create_Brain(self):
        pyrosim.Start_NeuralNetwork(f"brain_{self.myID}.nndf")
        pyrosim.Send_Sensor_Neuron(name = 0 , linkName = "Torso")
        pyrosim.Send_Sensor_Neuron(name = 1 , linkName = "BackLowerLeg")
        pyrosim.Send_Sensor_Neuron(name = 2 , linkName = "FrontLowerLeg")
        pyrosim.Send_Sensor_Neuron(name = 3 , linkName = "LeftLowerLeg")
        pyrosim.Send_Sensor_Neuron(name = 4 , linkName = "RightLowerLeg")

        pyrosim.Send_Motor_Neuron(name = 5 , jointName = "BackLeg_BackLowerLeg")
        pyrosim.Send_Motor_Neuron(name = 6 , jointName = "FrontLeg_FrontLowerLeg")
        pyrosim.Send_Motor_Neuron(name = 7 , jointName = "LeftLeg_LeftLowerLeg")
        pyrosim.Send_Motor_Neuron(name = 8 , jointName = "RightLeg_RightLowerLeg")
        pyrosim.Send_Motor_Neuron(name = 9 , jointName = "Torso_BackLeg")
        pyrosim.Send_Motor_Neuron(name = 10 , jointName = "Torso_FrontLeg")
        pyrosim.Send_Motor_Neuron(name = 11, jointName = "Torso_LeftLeg")
        pyrosim.Send_Motor_Neuron(name = 12, jointName = "Torso_RightLeg")

        for currentRow in range(c.numSensorNeurons):
            for currentColumn in range(c.numMotorNeurons):
                pyrosim.Send_Synapse( sourceNeuronName = currentRow , targetNeuronName = currentColumn+c.numSensorNeurons , weight = self.weights[currentRow][currentColumn] )
        pyrosim.End()
