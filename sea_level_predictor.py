import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Step 1: Read data from file
    df = pd.read_csv('epa-sea-level.csv')

    # Step 2: Create scatter plot
    plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'])

    # Step 3: Create first line of best fit (all data)
    slope_all, intercept_all, _, _, _ = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    
    # Step 4: Plot the first line of best fit for all data
    years_all = range(1880, 2051)
    sea_levels_all = [slope_all * year + intercept_all for year in years_all]
    plt.plot(years_all, sea_levels_all, label='Fit Line (All Data)', color='red')

    # Step 5: Create second line of best fit (from year 2000 onward)
    df_recent = df[df['Year'] >= 2000]
    slope_recent, intercept_recent, _, _, _ = linregress(df_recent['Year'], df_recent['CSIRO Adjusted Sea Level'])

    # Step 6: Plot the second line of best fit from 2000 onward
    years_recent = range(2000, 2051)
    sea_levels_recent = [slope_recent * year + intercept_recent for year in years_recent]
    plt.plot(years_recent, sea_levels_recent, label='Fit Line (2000-2050)', color='green')

    # Step 7: Add labels and title
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')
    plt.legend()

    # Step 8: Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()
