from simulation import SIMULATION
from robot import ROBOT
from world import WORLD
import sys


directOrGUI = sys.argv[1] if len(sys.argv) > 1 else None

simulation = SIMULATION(directOrGUI)
world = WORLD()
robot = ROBOT()

simulation.Run(directOrGUI)
