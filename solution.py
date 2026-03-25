import numpy as np
import pyrosim.pyrosim as pyrosim
import os
import random
import time

class SOLUTION:
    def __init__(self,nextAvailableID):
        self.myID = nextAvailableID
        self.weights = (np.random.rand(3,2))*2-1
    
    # def Evaluate(self,directOrGUI):
    #     self.Create_World()
    #     self.Create_Body()
    #     self.Create_Brain()
    #     os.system(f"python3 simulate.py {directOrGUI} {self.myID} &")

    #     while not os.path.exists("fitness.txt"):
    #         time.sleep(0.01)

    #     fitness_file = open(f"fitness{self.myID}.txt")
    #     self.fitness = float(fitness_file.readline())
    #     print(self.fitness)
    #     fitness_file.close()

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



    def Mutate(self):
        randomRow = random.randint(0,2)
        randomColumn = random.randint(0,1)
        self.weights[randomRow][randomColumn] = random.random() * 2 - 1 

    def Set_ID(self, nextAvailableID):
        self.myID = nextAvailableID
        






    
    def Create_World(self):
        pyrosim.Start_SDF("world.sdf")
        pyrosim.End()
    
    def Create_Body(self):
        pyrosim.Start_URDF("body.urdf")
        a=.25

        pyrosim.Send_Cube(name="Torso", pos=[0, 0, 1.5+a], size=[1, 1, 1])

        pyrosim.Send_Joint(name="Torso_BackLeg", parent="Torso", child="BackLeg", 
                        type="revolute", position=[-0.5, 0, 1+a])
        pyrosim.Send_Cube(name="BackLeg", pos=[-0.5, 0, -0.5], size=[1, 1, 1])

        pyrosim.Send_Joint(name="Torso_FrontLeg", parent="Torso", child="FrontLeg", 
                        type="revolute", position=[0.5, 0, 1+a])
        pyrosim.Send_Cube(name="FrontLeg", pos=[0.5, 0, -0.5], size=[1, 1, 1])

        pyrosim.End()

    def Create_Brain(self):
        pyrosim.Start_NeuralNetwork(f"brain_{self.myID}.nndf")
        pyrosim.Send_Sensor_Neuron(name = 0 , linkName = "Torso")
        pyrosim.Send_Sensor_Neuron(name = 1 , linkName = "BackLeg")
        pyrosim.Send_Sensor_Neuron(name = 2 , linkName = "FrontLeg")
        pyrosim.Send_Motor_Neuron( name = 3 , jointName = "Torso_BackLeg")
        pyrosim.Send_Motor_Neuron( name = 4 , jointName = "Torso_FrontLeg")

        for currentRow in range(3):
            for currentColumn in range(2):
                pyrosim.Send_Synapse( sourceNeuronName = currentRow , targetNeuronName = currentColumn+3 , weight = self.weights[currentRow][currentColumn] )
        pyrosim.End()





