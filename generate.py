import pyrosim.pyrosim as pyrosim


def Create_World():
    pyrosim.Start_SDF("world.sdf")
    x,y,z = -2,0,.5
    pyrosim.Send_Cube(name="Box", pos=[x,y,z], size=[1,1,1])
    pyrosim.End()

def Create_Robot():
    pyrosim.Start_URDF("body.urdf")
    x, y, z = 0, 0, 0.5
    pyrosim.Send_Cube(name="Torso", pos=[x, y, z], size=[1, 1, 1])
    pyrosim.End()


Create_World()
Create_Robot()