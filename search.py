import os
import parallelHillClimber
import time


# for i in range(2):
#     os.system("python3 generate.py")
#     os.system("python3 simulate.py")


for i in range(1):
    os.system("rm hidden_neuron_data.csv")
    os.system("rm recurrent_neuron_data.csv")

    phc = parallelHillClimber.PARALLEL_HILL_CLIMBER()

    phc.Evolve()
    
    phc.log_fitness_data()
    phc.Show_Best()


