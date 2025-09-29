import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

# load in the dataset
df = pd.read_csv("cars.csv")

# --------------------------------------------------- #
# Data Preprocessing

# filtering out cars with any missing values
df.dropna(inplace=True)

# convert "Model year" & "Cylinders" to integer fields
integer_fields = ["Model year", "Cylinders"]
for field in integer_fields:
    df[field] = df[field].apply(int)

grouped_by_make = df.groupby("Make")

# --------------------------------------------------- #
# Regression: engine size --> CO2 emissions
plt.scatter(df["Engine size (L)"], df["CO2 emissions (g/km)"])
plt.xlabel("Engine Size")
plt.ylabel("C02 Emissions")
plt.show()

result = linregress(df["Engine size (L)"], df["CO2 emissions (g/km)"])
print(result.pvalue)