# -*- coding: utf-8 -*-

import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator

# Read the CSV file
# file_path = "swim_activity.csv"  # Replace with your CSV file path
file_path = "/Users/changtang/Downloads/Activities.csv"
data = pd.read_csv(file_path)

# Convert "日期" column to datetime format
data["日期"] = pd.to_datetime(data["日期"])

# Filter data to include only rows from 2025 onwards
data = data[data["日期"].dt.year >= 2025]
data = data[data["日期"].dt.month >= 3]  # Filter to include only January and later

# Remove commas from numeric columns and convert them to numeric types
data["Average Heart Rate"] = pd.to_numeric(data["平均心率"], errors="coerce")
data["Max Heart Rate"] = pd.to_numeric(data["最大心率"], errors="coerce")
data["Average Swolf"] = pd.to_numeric(data["平均 Swolf"], errors="coerce")

# Create the plot
fig, ax = plt.subplots(figsize=(10, 6))

# Plot Average Heart Rate
ax.plot(data["日期"], data["Average Heart Rate"], label="Average Heart Rate", marker="o", color="blue")

# Plot Max Heart Rate
ax.plot(data["日期"], data["Max Heart Rate"], label="Max Heart Rate", marker="x", color="red")

# Plot Average Swolf
ax.plot(data["日期"], data["Average Swolf"], label="Average Swolf", marker="s", color="green")

# Set labels and title
ax.set_xlabel("Date")
ax.set_ylabel("Value", color="black")
ax.yaxis.set_major_locator(MultipleLocator(5))  # Set step value to 5 for the y-axis
ax.tick_params(axis="y", labelcolor="black")
ax.legend(loc="upper left")

# Add title and grid
plt.title("Heart Rate and Swolf Over Time")
plt.grid()

# Show the plot
plt.tight_layout()
plt.show()
