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
        #synaptic weights from sensor to hidden
        self.weights_s2h = (np.random.rand(c.numSensorNeurons,c.numhiddenNeurons))*2-1
        #synaptic weights from hidden to motor
        self.weights_h2m = (np.random.rand(c.numhiddenNeurons,c.numMotorNeurons))*2-1

    

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
        randomHidden = random.randint(0, c.numhiddenNeurons - 1)
        randomSensor = random.randint(0, c.numSensorNeurons - 1)
        randomMotor = random.randint(0, c.numMotorNeurons - 1)
        self.weights_s2h[randomSensor][randomHidden] = random.random() * 2 - 1 
        self.weights_h2m[randomHidden][randomMotor] = random.random() * 2 - 1 


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

        sensor_linkNames = ["Torso", "BackLowerLeg", "FrontLowerLeg", "LeftLowerLeg", "RightLowerLeg"]
        motor_jointNames = ["BackLeg_BackLowerLeg", "FrontLeg_FrontLowerLeg", "LeftLeg_LeftLowerLeg", "RightLeg_RightLowerLeg",
                            "Torso_BackLeg", "Torso_FrontLeg", "Torso_LeftLeg", "Torso_RightLeg"]

        for i in range(c.numSensorNeurons):
            pyrosim.Send_Sensor_Neuron(name = i , linkName = sensor_linkNames[i])
        
        for i in range(c.numhiddenNeurons):
            pyrosim.Send_Hidden_Neuron( name = i+c.numSensorNeurons )

        for i in range(c.numMotorNeurons):
            pyrosim.Send_Motor_Neuron(name = i + c.numSensorNeurons+c.numhiddenNeurons , jointName = motor_jointNames[i])

        



        for currentRow in range(c.numSensorNeurons):#sensor
            for currentColumn in range(c.numhiddenNeurons):#motor
                pyrosim.Send_Synapse( sourceNeuronName = currentRow , targetNeuronName = currentColumn+c.numSensorNeurons , weight = self.weights_s2h[currentRow][currentColumn] )
                
        for currentRow in range(c.numhiddenNeurons):#sensor
            for currentColumn in range(c.numMotorNeurons):#motor
                #check here for future issues when adding hidden neurons --> currentColumn+c.numSensorNeurons+c.numhiddenNeurons 
                pyrosim.Send_Synapse( sourceNeuronName = currentRow+c.numSensorNeurons , targetNeuronName = currentColumn+c.numSensorNeurons+c.numhiddenNeurons , weight = self.weights_h2m[currentRow][currentColumn] )
           

        pyrosim.End()
      
