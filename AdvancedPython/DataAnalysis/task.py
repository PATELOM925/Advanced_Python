import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import csv
import seaborn as sns
from datetime import datetime

df = pd.read_csv("space_travellers.csv")
print("data frane: ",df)
df.dropna(inplace=True)
df = df.drop_duplicates()
df.isnull().sum()
df["Date"] = pd.to_datetime(df["Date"])

print(df.head(4))
print(df.tail(4))

print("Basic statistics:")
print(df.describe())

#nationality count
nationality_counts = df["Nationality"].value_counts()
print(nationality_counts)

#timeperiod
earliest_mission = df["Date"].min()
latest_mission = df["Date"].max()
print("Earliest Mission:", earliest_mission)
print("Latest Mission:", latest_mission)

#time
earliest_mission = df["Date"].min()
latest_mission = df["Date"].max()
print("Earliest Mission:", earliest_mission)
print("Latest Mission:", latest_mission)

#number of missions per year
df["Year"] = df["Date"].dt.year
missions_per_year = df["Year"].value_counts().sort_index()
missions_per_year.plot(kind="bar", xlabel="Year", ylabel="Number of Missions")
plt.show()

#time series Plot
dates = df['Date']
plt.figure(figsize=(12, 6))
plt.plot(dates, range(1, len(dates) + 1), marker='*', linestyle='--')
plt.xlabel('Date')
plt.ylabel("No. of Astronauts")
plt.title('Astronauts in Space')
plt.show()



