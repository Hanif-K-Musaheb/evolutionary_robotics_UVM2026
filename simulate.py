import pybullet as p
import pybullet_data
import time
import pyrosim.pyrosim as pyrosim
import numpy


steps_in_sim=200


physicsClient = p.connect(p.GUI)
p.setAdditionalSearchPath(pybullet_data.getDataPath())
#p.configureDebugVisualizer(p.COV_ENABLE_GUI,0)
p.setGravity(0,0,-19.8)
planeId = p.loadURDF("plane.urdf")# the floor of the simulation
robotId = p.loadURDF("body.urdf")
p.loadSDF("world.sdf")

pyrosim.Prepare_To_Simulate(robotId)

#sensors
backLegSensorValues = numpy.zeros(steps_in_sim)
frontLegSensorValues = numpy.zeros(steps_in_sim)



for i in range(steps_in_sim): 
    
    p.stepSimulation()

    backLegTouch = pyrosim.Get_Touch_Sensor_Value_For_Link("BackLeg")
    backLegSensorValues[i]=backLegTouch

    frontLegTouch = pyrosim.Get_Touch_Sensor_Value_For_Link("FrontLeg")
    frontLegSensorValues[i]=frontLegTouch

    pyrosim.Set_Motor_For_Joint(
        bodyIndex = robotId,
        jointName = b'Torso_BackLeg',
        controlMode = p.POSITION_CONTROL,
        targetPosition = 0.0,
        maxForce = 500)

    time.sleep(1/120)
    

p.disconnect()

numpy.save("data/backLegSensorValues.npy",backLegSensorValues)
numpy.save("data/frontLegSensorValues.npy",frontLegSensorValues)
