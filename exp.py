import pandas as pd

df = pd.read_csv("cars.csv")
df.dropna(inplace=True)
print(df.shape)
print(df.head(10))