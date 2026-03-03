import numpy as np
import constants as c
import pybullet as p
import pyrosim.pyrosim as pyrosim

class MOTOR:
    def __init__(self,jointName):
        self.jointName = jointName
        self.motor_values = np.zeros(c.steps_in_sim)
        self.Prepare_To_Act()


    def Prepare_To_Act(self):
        self.amplitude = c.amplitude_B
        self.frequency=c.frequency_B
        self.offset=c.phaseOffset_B

        if self.jointName == b'Torso_BackLeg':
            self.frequency = self.frequency/2

        # generate vector of sinusoidally varying values
        firstVector = np.linspace(0, np.pi * 2, c.steps_in_sim)
        # Back Leg
        for ind, each in enumerate(firstVector):
            self.motor_values[ind] = self.amplitude * \
                np.sin(self.frequency * each + self.offset)
    
    def set_value(self,desiredAngle,robotId):
        pyrosim.Set_Motor_For_Joint(
        bodyIndex = robotId,
        jointName = self.jointName,
        controlMode = p.POSITION_CONTROL,
        targetPosition = desiredAngle,
        maxForce = c.max_force)

    def Save_Value(self):
        dst = 'data/' + self.jointName + 'Motor'
        np.save(dst, self.motor_values)
    
       