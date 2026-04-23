import os
import parallelHillClimber


# for i in range(2):
#     os.system("python3 generate.py")
#     os.system("python3 simulate.py")

os.system("rm hidden_neuron_data.csv")
os.system("rm recurrent_neuron_data.csv")




phc = parallelHillClimber.PARALLEL_HILL_CLIMBER()

phc.Evolve()
phc.Show_Best()
