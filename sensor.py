import numpy as np
import constants as c
import pyrosim.pyrosim as pyrosim

class SENSOR:
    def __init__(self,linkName):
        self.linkName = linkName
        self.values = np.zeros(c.steps_in_sim)

    def Get_Value(self,i):
        self.values[i]=pyrosim.Get_Touch_Sensor_Value_For_Link(self.linkName)
        if i==c.steps_in_sim-1:
            print(self.values)
    
    def Save_Value(self):
        dst = 'data/' + self.linkName + 'Sensor'
        np.save(dst, self.values)
