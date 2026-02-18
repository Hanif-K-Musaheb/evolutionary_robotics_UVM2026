import numpy as np
import matplotlib.pyplot as plt

# backLegSensorValues = np.load("data/backLegSensorValues.npy")
# frontLegSensorValues = np.load("data/frontLegSensorValues.npy")
target_angles_B = np.load("data/target_angles_B.npy")
target_angles_F = np.load("data/target_angles_F.npy")


# plt.plot(backLegSensorValues,label = "Back leg", linewidth=4)
# plt.plot(frontLegSensorValues,label="Front leg")
plt.plot(target_angles_B,label="Target Angles B")
plt.plot(target_angles_F,label="Target Angles F")


plt.legend()
plt.show()