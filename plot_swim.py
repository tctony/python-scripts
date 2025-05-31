import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime
import matplotlib.ticker as ticker
import numpy as np

# Function to format seconds to min:sec
def format_time(seconds, pos):
    minutes = int(seconds // 60)
    seconds = int(seconds % 60)
    return f"{minutes}:{seconds:02d}"

# Read the CSV file with header
file_path = "/Users/changtang/Downloads/每次进步一点点-自由泳.csv"
data = pd.read_csv(file_path)

# Convert the "Date" column to datetime format
data["日期"] = pd.to_datetime(data["日期"], format="%Y%m%d")

# Convert "Pace" from fraction of a day to seconds
data["配速(s)"] = data["配速"] * 24 * 60 * 60

# Plot the data
fig, ax1 = plt.subplots()

# Plot Distance on the primary y-axis
ax1.set_xlabel("Date")
ax1.set_ylabel("Distance (m)", color="tab:blue")
ax1.plot(data["日期"], data["距离"], label="Distance", color="tab:blue", marker="o")
ax1.tick_params(axis="y", labelcolor="tab:blue")

# Create a secondary y-axis for Pace
ax2 = ax1.twinx()
ax2.set_ylabel("Pace (min:sec)", color="tab:orange")
ax2.plot(data["日期"], data["配速(s)"], label="Pace", color="tab:orange", marker="x")
ax2.tick_params(axis="y", labelcolor="tab:orange")
ax2.yaxis.set_major_formatter(ticker.FuncFormatter(format_time))

# Set fixed 5-second interval ticks for pace
min_pace = np.floor(data["配速(s)"].min() / 5) * 5  # Round down to nearest 5 seconds
max_pace = np.ceil(data["配速(s)"].max() / 5) * 5   # Round up to nearest 5 seconds
ax2.set_yticks(np.arange(min_pace, max_pace + 5, 5))  # 5-second intervals

# Add a title and grid
plt.title("Swim Data: Distance and Pace Over Time")
fig.tight_layout()
plt.grid()

# Show the plot
plt.show()
