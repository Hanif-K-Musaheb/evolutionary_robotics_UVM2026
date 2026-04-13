import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('hidden_neuron_data.csv', header=None)

df.columns = ['Time Step', 'Neuron 1', 'Neuron 2', 'Neuron 3']

df.set_index('Time Step').plot(figsize=(10, 6))

plt.title('Hidden Neuron Activity Over Time')
plt.ylabel('Neuron Value')
plt.grid(True)
plt.show()