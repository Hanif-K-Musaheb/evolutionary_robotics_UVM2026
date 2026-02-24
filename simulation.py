import constants as c
import pybullet as p
import pybullet_data
import pyrosim.pyrosim as pyrosim
from robot import ROBOT
import time
from world import WORLD


class SIMULATION:
    def __init__(self):
        self.robot=ROBOT()
        self.world = WORLD()

        self.physicsClient = p.connect(p.GUI)
        p.setAdditionalSearchPath(pybullet_data.getDataPath())

        p.setGravity(0,0,-19.8)
        p.loadSDF("world.sdf")
        self.planeId = p.loadURDF("plane.urdf")
        self.robotId = p.loadURDF("body.urdf")

        pyrosim.Prepare_To_Simulate(self.robotId)
        self.robot.Prepare_To_Sense()
        self.robot.Prepare_To_Act()
       
    
    def __del__(self):
        p.disconnect()
    
    def Run(self):
        # keep the world open for c.iterations long
        for it in range(c.steps_in_sim):
            p.stepSimulation()
            self.robot.sense(it)
            self.robot.Act(it,self.robotId)

            time.sleep(c.time_step)

        
    

      
        