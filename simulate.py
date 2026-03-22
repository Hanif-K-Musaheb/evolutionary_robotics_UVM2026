from simulation import SIMULATION
from robot import ROBOT
from world import WORLD
import sys


directOrGUI = sys.argv[1] if len(sys.argv) > 1 else None
solutionID = sys.argv[2]

simulation = SIMULATION(directOrGUI,solutionID)
world = WORLD()
robot = ROBOT(solutionID)

simulation.Run(directOrGUI)
