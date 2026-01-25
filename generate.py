import pyrosim.pyrosim as pyrosim

pyrosim.Start_SDF("boxes.sdf")
x,y,z = 0,0,.5
x2,y2,z2=1,0,1.5
pyrosim.Send_Cube(name="Box", pos=[x,y,z], size=[1,1,1])
pyrosim.Send_Cube(name="Box2", pos=[x2,y2,z2], size=[1,1,1])



pyrosim.End()