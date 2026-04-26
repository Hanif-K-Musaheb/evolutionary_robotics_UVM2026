import pandas as pd
import matplotlib.pyplot as plt

# 1. Load the CSV file
# index_col=0 tells pandas to use the first column (Robot ID) as the row labels
df = pd.read_csv('brainacs_fitness_data.csv', index_col=0)

# 2. Transpose the data
# This flips the table so that rows become timesteps and columns become Robot IDs.
df_transposed = df.T

# 3. Create the plot
# Setting a larger figure size (14x7 inches) helps when viewing many timesteps
plt.figure(figsize=(14, 7))

# Plot all columns (every robot gets its own line)
# alpha=0.6 makes the lines slightly transparent so it's easier to see overlapping paths
plt.plot(df_transposed.values, alpha=0.6)

# 4. Add labels and styling
plt.title('Robot Fitness Over 1000 Timesteps')
plt.xlabel('Timestep')
plt.ylabel('Fitness')
plt.grid(True, linestyle='--', alpha=0.5)

# Note: With 110 robots, a legend will completely cover the graph. 
# It is usually best to leave it off for this many lines.

# 5. Show the graph
plt.tight_layout()
plt.show()