import pandas as pd

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

print(df["Make"].value_counts())
grouped_by_make = df.groupby("Make")