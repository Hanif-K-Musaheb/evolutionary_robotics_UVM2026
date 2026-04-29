import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D  # This helps us build a custom legend


def display_graph(data,alpha,version):
    df = pd.read_csv(data, header=None)
    df_transposed = df.T

    plt.figure(figsize=(14, 7))
    plt.plot(df_transposed.values, alpha=alpha)
    plt.title(f"{version} Fitness Over Timesteps")
    plt.xlabel('Timestep')
    plt.ylabel('Fitness')
    plt.grid(True, linestyle='--', alpha=0.5)


    plt.tight_layout()
    plt.show()

def graph_comparison():
    df_v1 = pd.read_csv('peak_normal_brain_fitness_data.csv', header=None)
    df_v2 = pd.read_csv('peak_brainacs_fitness_data.csv', header=None)

    df_v1_transposed = df_v1.T
    df_v2_transposed = df_v2.T
    plt.figure(figsize=(14, 7))


    plt.plot(df_v1_transposed.values, color='blue', alpha=0.2)


    plt.plot(df_v2_transposed.values, color='red', alpha=0.2)


    legend_elements = [
        Line2D([0], [0], color='blue', lw=4, label='normal brain (5-8) 1'),
        Line2D([0], [0], color='red', lw=4, label='brainiac (5-3-3-8)')
    ]
    plt.legend(handles=legend_elements, loc='upper left')


    plt.title('Fitness Comparison: Brainiac vs. Normal Brain')
    plt.xlabel('Timestep')
    plt.ylabel('Fitness')
    plt.grid(True, linestyle='--', alpha=0.5)

    plt.tight_layout()
    plt.show()

def graph_comparison_avg():
    df_v1 = pd.read_csv('peak_normal_brain_fitness_data.csv', header=None)
    df_v2 = pd.read_csv('peak_brainacs_fitness_data.csv', header=None)

    df_v1_transposed = df_v1.T
    df_v2_transposed = df_v2.T


    v1_average = df_v1_transposed.mean(axis=1)
    v2_average = df_v2_transposed.mean(axis=1)

    plt.figure(figsize=(14, 7))


    plt.plot(df_v1_transposed.values, color='blue', alpha=0.15)
    plt.plot(df_v2_transposed.values, color='red', alpha=0.15)


    plt.plot(v1_average, color='darkblue', linewidth=3)
    plt.plot(v2_average, color='darkred', linewidth=3)

    legend_elements = [
        Line2D([0], [0], color='blue', alpha=0.3, lw=4, label='normal brain (Individuals)'),
        Line2D([0], [0], color='darkblue', lw=3, label='normal brain (Average)'),
        Line2D([0], [0], color='red', alpha=0.3, lw=4, label='brainiac (Individuals)'),
        Line2D([0], [0], color='darkred', lw=3, label='brainiac (Average)')
    ]
    plt.legend(handles=legend_elements, loc='upper left')

    plt.title('Fitness Comparison: normal brain 1 vs. brainiac with averages')
    plt.xlabel('Timestep')
    plt.ylabel('Fitness')
    plt.grid(True, linestyle='--', alpha=0.5)

    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    display_graph('peak_normal_brain_fitness_data.csv',.2,'normal brain')
    display_graph('peak_brainacs_fitness_data.csv',.2,'brainiac')
    graph_comparison()
    graph_comparison_avg()




