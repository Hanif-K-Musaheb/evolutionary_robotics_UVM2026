# import pybullet as p
# import pybullet_data
# import time
# import pyrosim.pyrosim as pyrosim
# import numpy as np
# import math
# import random
# import constants as c




# physicsClient = p.connect(p.GUI)
# p.setAdditionalSearchPath(pybullet_data.getDataPath())
# #p.configureDebugVisualizer(p.COV_ENABLE_GUI,0)
# p.setGravity(0,0,-19.8)
# planeId = p.loadURDF("plane.urdf")# the floor of the simulation
# robotId = p.loadURDF("body.urdf")
# p.loadSDF("world.sdf")

# pyrosim.Prepare_To_Simulate(robotId)

# #####################

# #sensors
# backLegSensorValues = np.zeros(c.steps_in_sim)
# frontLegSensorValues = np.zeros(c.steps_in_sim)

# linearly_spaced_values = np.linspace(0, 2 * np.pi, c.steps_in_sim)#vector for movement vals



# target_angles_F=(c.amplitude_F*np.sin((linearly_spaced_values*c.frequency_F+c.phaseOffset_F)))



# target_angles_B=(c.amplitude_B*np.sin((linearly_spaced_values*c.frequency_B+c.phaseOffset_B)))


# np.save("data/target_angles_B.npy",target_angles_B)
# np.save("data/target_angles_F.npy",target_angles_F)
# # quit()

# for i in range(c.steps_in_sim): 
    
#     p.stepSimulation()

#     backLegTouch = pyrosim.Get_Touch_Sensor_Value_For_Link("BackLeg")
#     backLegSensorValues[i]=backLegTouch

#     frontLegTouch = pyrosim.Get_Touch_Sensor_Value_For_Link("FrontLeg")
#     frontLegSensorValues[i]=frontLegTouch

#     targetPosition = random.uniform(-1,1)*math.pi/2

#     pyrosim.Set_Motor_For_Joint(
#         bodyIndex = robotId,
#         jointName = b'Torso_BackLeg',
#         controlMode = p.POSITION_CONTROL,
#         targetPosition = target_angles_B[i],
#         maxForce = c.max_force)
    
#     pyrosim.Set_Motor_For_Joint(
#         bodyIndex = robotId,
#         jointName = b'Torso_FrontLeg',
#         controlMode = p.POSITION_CONTROL,
#         targetPosition = target_angles_F[i],
#         maxForce = c.max_force)

#     time.sleep(c.time_step)
    

# p.disconnect()

# np.save("data/backLegSensorValues.npy",backLegSensorValues)
# np.save("data/frontLegSensorValues.npy",frontLegSensorValues)







import constants as c
from robot import ROBOT
from simulation import SIMULATION
from world import WORLD

simulation = SIMULATION()
world = WORLD()
robot = ROBOT()

simulation.Run()
