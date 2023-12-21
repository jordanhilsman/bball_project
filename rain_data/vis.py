import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

df = pd.read_csv("kerala.csv")

month_dict = {
    "JAN": "January",
    "FEB": "February",
    "MAR": "March",
    "APR": "April",
    "MAY": "May",
    "JUN": "June",
    "JUL": "July",
    "AUG": "August",
    "SEP": "September",
    "OCT": "October",
    "NOV": "November",
    "DEC": "December",
}


months = ["JAN", "FEB", "MAR", "APR", "MAY", "JUN", "JUL", "AUG", "SEP", "OCT", "NOV", "DEC"]

minima = []
maxima = []
avgs = []
for month in months:
    month_min = min(df[month])
    month_max = max(df[month])
    month_avg = np.mean(df[month])
    dicted = month_dict[month]
    minima.append(month_min)
    maxima.append(month_max)
    avgs.append(month_avg)

plt.figure(figsize=(10,6))

sns.lineplot(x=month_dict.values(), y=minima, label="Minimums")
sns.lineplot(x=month_dict.values(), y=maxima, label="Maximums")
sns.lineplot(x=month_dict.values(), y=avgs, label="Average")

plt.title("Maximum, Minimum, and Average Monthly Rainfall Values")
plt.xlabel("Month")
plt.ylabel("Rainfall (inches)")

plt.legend()

plt.show()

month_count = {
    "JAN":0,
    "FEB":0,
    "MAR":0,
    "APR":0,
    "MAY":0,
    "JUN":0,
    "JUL":0,
    "AUG":0,
    "SEP":0,
    "OCT":0,
    "NOV":0,
    "DEC":0
        }
for index, row in df.iterrows():
    ph = 0
    for month in months:
        if row[month] > ph:
            ph = row[month]

    print(max(row))
