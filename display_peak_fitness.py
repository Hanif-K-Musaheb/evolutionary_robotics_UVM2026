import pandas as pd
import matplotlib.pyplot as plt

# 1. Load the CSV
# We remove index_col=0. 
# I added header=None assuming your CSV is purely data and doesn't have a row of column names at the very top. 
# (If it does have column names, just remove the `header=None` part!)
df = pd.read_csv('peak_brainacs_fitness_data.csv', header=None)

# 2. Transpose the data
df_transposed = df.T

# 3. Create the plot
plt.figure(figsize=(14, 7))

# Plot all columns
plt.plot(df_transposed.values, alpha=0.6)

# 4. Add labels and styling
plt.title('Robot Fitness Over Timesteps')
plt.xlabel('Timestep')
plt.ylabel('Fitness')
plt.grid(True, linestyle='--', alpha=0.5)

# 5. Show the graph
plt.tight_layout()
plt.show()