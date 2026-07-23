import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress


def draw_plot():
    # Import data
    df = pd.read_csv("epa-sea-level.csv")

    # Create scatter plot
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.scatter(df["Year"], df["CSIRO Adjusted Sea Level"])

    # First line of best fit (1880–2050)
    res = linregress(df["Year"], df["CSIRO Adjusted Sea Level"])

    years = pd.Series(range(1880, 2051))
    ax.plot(years, res.slope * years + res.intercept, "r")

    # Second line of best fit (2000–2050)
    recent = df[df["Year"] >= 2000]

    res_recent = linregress(
        recent["Year"],
        recent["CSIRO Adjusted Sea Level"],
    )

    years_recent = pd.Series(range(2000, 2051))
    ax.plot(
        years_recent,
        res_recent.slope * years_recent + res_recent.intercept,
        "g",
    )

    # Labels and title
    ax.set_xlabel("Year")
    ax.set_ylabel("Sea Level (inches)")
    ax.set_title("Rise in Sea Level")

    fig.savefig("sea_level_plot.png")

    return fig
