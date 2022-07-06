import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress


def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')

    # Create scatter plot
    x = df['Year']
    y = df['CSIRO Adjusted Sea Level']

    fig, ax = plt.subplots(figsize=(14, 7))
    plt.scatter(x, y)


    # Create first line of best fit (years: 1880 to 2050)
    res_1 = linregress(x, y)
    x_pred = pd.Series(i for i in range(1880, 2051))
    y_pred = res_1.slope * x_pred + res_1.intercept  # m = i*a + b
    plt.plot(x_pred, y_pred, 'r', linewidth=2)

    # Create second line of best fit (years: 2000 to 2050)
    df_2000_2050 = df.copy()
    df_2000_2050 = df.loc[df_2000_2050['Year'] >= 2000]
    x_2000_2050 = df_2000_2050['Year']
    y_2000_2050 = df_2000_2050['CSIRO Adjusted Sea Level']

    res_2 = linregress(x_2000_2050, y_2000_2050)
    x_pred_2000_2050 = pd.Series(i for i in range(2000, 2051))
    y_pred_2000_2050 = res_2.slope * x_pred_2000_2050 + res_2.intercept  # m = i*a + b
    plt.plot(x_pred_2000_2050, y_pred_2000_2050, 'g', linewidth=2)

    # Add labels and title
    ax.set_title('Rise in Sea Level', pad=10.0, fontsize=14)
    ax.set_xlabel('Year', labelpad=10.0, fontsize=12)
    ax.set_ylabel('Sea Level (inches)', labelpad=10.0, fontsize=12)
    ax.grid(True, color='#c0c0c0', linestyle='--', linewidth=0.5)

    # Save plot and return data for testing
    plt.savefig('sea_level_plot.png')
    return plt.gca()
