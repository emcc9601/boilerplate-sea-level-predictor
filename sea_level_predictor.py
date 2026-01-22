import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress
import seaborn as sns

def draw_plot():
    # Read data from file
    df = pd.read_csv("epa-sea-level.csv")

    # Create scatter plot
    plt.scatter(df["Year"], df["CSIRO Adjusted Sea Level"], s=5, c=["#000000"])

    # Create first line of best fit
    result = linregress(df["Year"], df["CSIRO Adjusted Sea Level"])

    tempYears = df["Year"].tolist()
    tempLevel = df["CSIRO Adjusted Sea Level"].tolist()
    year = tempYears[len(tempYears)-1]

    while year != 2050:
        year += 1

        predicted_sea_level = result.slope * year + result.intercept
        tempYears.append(year)
        tempLevel.append(predicted_sea_level)

    plt.plot(tempYears, tempLevel, c="red", linewidth=1)

    # Create second line of best fit
    result = linregress(df["Year"], df["CSIRO Adjusted Sea Level"])

    plt.axline(xy1=(df["Year"].tolist()[0], df["CSIRO Adjusted Sea Level"].tolist()[0]), slope=result.slope, c="green", linewidth=1)

    # Add labels and title
    plt.xlim(right=2050)
    plt.ylim(top=result.slope * (2050-df["Year"].tolist()[0]))

    plt.xlabel("Year")
    plt.ylabel("Sea Level (inches)")
    plt.title("Rise in Sea Level")
    plt.xticks([1850, 1875, 1925, 1950, 1975, 2000, 2025, 2050, 2075])
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()