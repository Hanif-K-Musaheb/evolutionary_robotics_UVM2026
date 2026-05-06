import numpy

steps_in_sim=1000#1000
max_force=50
time_step = 0#(1/(60*8))/100

dist2ground=.5

numberOfGenerations =100 #10
populationSize= 10

#front leg settings
amplitude_F =  -numpy.pi/2
frequency_F = 20#30
phaseOffset_F = 0


#back leg settings
amplitude_B = numpy.pi/2
frequency_B = 20
phaseOffset_B = 0

numSensorNeurons=5
numMotorNeurons=8
numhiddenNeurons=3
numRecursiveNeurons=numhiddenNeurons

motorJointRange=.2