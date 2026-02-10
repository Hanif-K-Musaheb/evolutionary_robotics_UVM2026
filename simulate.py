import pybullet as p
import pybullet_data
import time
import pyrosim.pyrosim as pyrosim
import numpy

steps_in_sim=100


physicsClient = p.connect(p.GUI)
p.setAdditionalSearchPath(pybullet_data.getDataPath())
#p.configureDebugVisualizer(p.COV_ENABLE_GUI,0)
p.setGravity(0,0,-19.8)
planeId = p.loadURDF("plane.urdf")# the floor of the simulation
robotId = p.loadURDF("body.urdf")
p.loadSDF("world.sdf")

pyrosim.Prepare_To_Simulate(robotId)
backLegSensorValues = numpy.zeros(steps_in_sim)
print(backLegSensorValues)


for i in range(steps_in_sim): 
    
    p.stepSimulation()

    backLegTouch = pyrosim.Get_Touch_Sensor_Value_For_Link("BackLeg")
    backLegSensorValues[i]=backLegTouch

    time.sleep(1/120)
    

p.disconnect()

numpy.save("data/backLegSensorValues.npy",backLegSensorValues)
