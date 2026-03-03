import math

steps_in_sim=1000#1000
max_force=60
time_step = 1/(60*8)

#front leg settings
amplitude_F = math.pi/3
frequency_F = 0#30
phaseOffset_F = 0


#back leg settings
amplitude_B = math.pi/3
frequency_B = 10
phaseOffset_B = 0.5*math.pi