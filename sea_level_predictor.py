import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')

    # Create scatter plot
    plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'], color='blue', label='Observed')

    # Create first line of best fit
    x1 = df['Year']
    y1 = df['CSIRO Adjusted Sea Level']
    slope, intercept, r_value, p_value, std_err = linregress(x1, y1)
    years_extended = pd.Series(range(1880, 2051))  # Years from 1880 to 2050
    plt.plot(years_extended, intercept + slope * years_extended, 'r', label='Fit Line 1880-2050')

    # Create second line of best fit for years from 2000 onwards
    df_2000 = df[df['Year'] >= 2000]
    x2 = df_2000['Year']
    y2 = df_2000['CSIRO Adjusted Sea Level']
    slope_2000, intercept_2000, r_value_2000, p_value_2000, std_err_2000 = linregress(x2, y2)

    # Use years from 2000 to 2050 for the second line of best fit
    years_extended_2000 = pd.Series(range(2000, 2051))  # Years from 2000 to 2050
    plt.plot(years_extended_2000, intercept_2000 + slope_2000 * years_extended_2000, 'g', label='Fit Line 2000-2050')

    # Add labels and title
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')
    plt.legend()

    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()
