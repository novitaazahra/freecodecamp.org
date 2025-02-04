import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# 1 - Assuming the dataset is loaded from a CSV, for example
df = pd.read_csv('medical_examination.csv')  # Load your data file here

# 2 - Adding the 'overweight' column if it's not already present
df['overweight'] = df['weight'] / (df['height'] / 100) ** 2 > 25  # Assuming BMI calculation logic

# 3 - Clean or preprocess the dataset if needed
df = df.dropna()  # Example of handling missing data

# 4 - Function to create the categorical plot
def draw_cat_plot():
    # 5 - Prepare categorical plot data, for example, using groupby
    df_cat = df.groupby(['active', 'overweight']).size().reset_index(name='total')

    # 6 - Create the categorical plot (using a barplot as an example)
    fig, ax = plt.subplots(figsize=(8, 6))  # Create a figure and axis
    sns.barplot(x='active', y='total', hue='overweight', data=df_cat, ax=ax)

    # 7 - Set labels and title for the plot
    ax.set_xlabel('variable')  # X-axis label
    ax.set_ylabel('total')     # Y-axis label
    ax.set_title('Active vs Overweight')  # Plot title

    # 8 - Customize further if needed, e.g., legend or formatting

    # 9 - Save the figure as an image
    fig.savefig('catplot.png')
    return fig

# 10 - Function to create the heatmap
def draw_heat_map():
    # 11 - Calculate the correlation matrix for numerical columns
    df_heat = df.corr()

    # 12 - Set a mask for the upper triangle (optional)
    mask = np.triu(np.ones_like(df_heat, dtype=bool))

    # 13 - Define the color palette for the heatmap
    cmap = sns.diverging_palette(230, 20, as_cmap=True)

    # 14 - Create the heatmap plot
    fig, ax = plt.subplots(figsize=(10, 8))  # Figure size
    sns.heatmap(df_heat, mask=mask, cmap=cmap, annot=True, fmt='.2f', ax=ax, linewidths=0.5)

    # 15 - Set title and labels
    ax.set_title('Correlation Heatmap')

    # 16 - Save the heatmap as an image
    fig.savefig('heatmap.png')
    return fig
