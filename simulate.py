import pybullet as p
import pybullet_data
import time
import pyrosim.pyrosim as pyrosim
import numpy as np
import math
import random


steps_in_sim=1000


physicsClient = p.connect(p.GUI)
p.setAdditionalSearchPath(pybullet_data.getDataPath())
#p.configureDebugVisualizer(p.COV_ENABLE_GUI,0)
p.setGravity(0,0,-19.8)
planeId = p.loadURDF("plane.urdf")# the floor of the simulation
robotId = p.loadURDF("body.urdf")
p.loadSDF("world.sdf")

pyrosim.Prepare_To_Simulate(robotId)

#sensors
backLegSensorValues = np.zeros(steps_in_sim)
frontLegSensorValues = np.zeros(steps_in_sim)

pi=math.pi

max_force=60

linearly_spaced_values = np.linspace(0, 2 * np.pi, steps_in_sim)#vector for movement vals

#front leg
amplitude_F = pi/3
frequency_F = 30
phaseOffset_F = 0
target_angles_F=(amplitude_F*np.sin((linearly_spaced_values*frequency_F+phaseOffset_F)))


#back leg
amplitude_B = pi/3
frequency_B = 10
phaseOffset_B = 0.5*pi
target_angles_B=(amplitude_B*np.sin((linearly_spaced_values*frequency_B+phaseOffset_B)))


np.save("data/target_angles_B.npy",target_angles_B)
np.save("data/target_angles_F.npy",target_angles_F)
# quit()

for i in range(steps_in_sim): 
    
    p.stepSimulation()

    backLegTouch = pyrosim.Get_Touch_Sensor_Value_For_Link("BackLeg")
    backLegSensorValues[i]=backLegTouch

    frontLegTouch = pyrosim.Get_Touch_Sensor_Value_For_Link("FrontLeg")
    frontLegSensorValues[i]=frontLegTouch

    targetPosition = random.uniform(-1,1)*pi/2

    pyrosim.Set_Motor_For_Joint(
        bodyIndex = robotId,
        jointName = b'Torso_BackLeg',
        controlMode = p.POSITION_CONTROL,
        targetPosition = target_angles_B[i],
        maxForce = max_force)
    
    pyrosim.Set_Motor_For_Joint(
        bodyIndex = robotId,
        jointName = b'Torso_FrontLeg',
        controlMode = p.POSITION_CONTROL,
        targetPosition = target_angles_F[i],
        maxForce = max_force)

    time.sleep(1/(60*8))
    

p.disconnect()

np.save("data/backLegSensorValues.npy",backLegSensorValues)
np.save("data/frontLegSensorValues.npy",frontLegSensorValues)
