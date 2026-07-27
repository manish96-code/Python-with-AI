import pandas as pd

df = pd.read_json("pandas/data.json")

# new_df = df.dropna()
# print(new_df)

df.fillna(10, inplace=True)
print(df)