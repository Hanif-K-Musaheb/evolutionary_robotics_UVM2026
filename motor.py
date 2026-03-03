import numpy as np
import constants as c
import pybullet as p
import pyrosim.pyrosim as pyrosim

class MOTOR:
    def __init__(self,jointName):
        self.jointName = jointName
        self.motor_values = np.zeros(c.steps_in_sim)

    
    def set_value(self,desiredAngle,robotId):
        pyrosim.Set_Motor_For_Joint(
        bodyIndex = robotId,
        jointName = self.jointName,
        controlMode = p.POSITION_CONTROL,
        targetPosition = desiredAngle,
        maxForce = c.max_force)


    
       