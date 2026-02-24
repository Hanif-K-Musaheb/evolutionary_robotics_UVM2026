import numpy as np
import constants as c

class MOTOR:
    def __init__(self,jointName):
        self.jointName = jointName
        self.motor_values = np.zeros(c.steps_in_sim)
        self.Prepare_To_Act()

    def Prepare_To_Act(self):
        self.amplitude = c.amplitude_B
        self.frequency=c.frequency_B
        self.offset=c.phaseOffset_B