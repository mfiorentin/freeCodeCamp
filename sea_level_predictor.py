# link to replit code: https://replit.com/@MauricioFiorent/boilerplate-sea-level-predictor

import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv', sep=',')

    # Create scatter plot
    plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'])

    # Create first line of best fit
    first_line = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    xvalue = pd.DataFrame(list(range(df['Year'].iloc[0], 2051)))
    plt.plot(xvalue, xvalue * first_line.slope + first_line.intercept)

    # Create second line of best fit
    df_2000 = df[df['Year'] >= 2000]
    xvalue_2 = pd.DataFrame(list(range(df_2000['Year'].iloc[0], 2051)))
    second_line = linregress(df_2000['Year'], df_2000['CSIRO Adjusted Sea Level'])
    plt.plot(xvalue_2, xvalue_2 * second_line.slope + second_line.intercept)

    # Add labels and title
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()
