import constants as c
import pybullet as p
import pybullet_data
import pyrosim.pyrosim as pyrosim
from robot import ROBOT
import time
from world import WORLD


class SIMULATION:
    def __init__(self,directOrGUI):
        self.robot=ROBOT()
        self.world = WORLD()

        print(directOrGUI,'='*20)
        if directOrGUI== "DIRECT" or directOrGUI == None:
            self.physicsClient = p.connect(p.DIRECT)#p.GUI)
        else:
            self.physicsClient = p.connect(p.GUI)

        p.setAdditionalSearchPath(pybullet_data.getDataPath())

        p.setGravity(0,0,-9.8)
        p.loadSDF("world.sdf")
        self.planeId = p.loadURDF("plane.urdf")
        self.robotId = p.loadURDF("body.urdf")

        pyrosim.Prepare_To_Simulate(self.robotId)
        self.robot.Prepare_To_Sense()
        self.robot.Prepare_To_Act()

    def Get_fitness(self):
        self.robot.Get_Fitness(self.robotId)
        
       
    
    def __del__(self):
        p.disconnect()
    
    def Run(self,directOrGUI):
        # keep the world open for c.iterations long
        for it in range(c.steps_in_sim):
            p.stepSimulation()
            self.robot.sense(it)
            self.robot.Think()
            self.robot.Act(it,self.robotId)

            self.robot.Get_Fitness(self.robotId)

            
            if directOrGUI!= "DIRECT" and directOrGUI!= None:time.sleep(c.time_step)
            

    

        
    

      
        