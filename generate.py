import pyrosim.pyrosim as pyrosim

pyrosim.Start_SDF("box.sdf")

pyrosim.Send_Cube(name="Box", pos=[0,0,0], size=[5,5,5])

pyrosim.End()