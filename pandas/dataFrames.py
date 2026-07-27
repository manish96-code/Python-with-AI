import pandas as pd

data = {
    "2021": [100, 200, 300],
    "2022": [150, 250, 350],
    "2023": [200, 300, 400],
    "2024": [250, 350, 450]
}

myNewData = pd.DataFrame(data, index=["India", "USA", "UK"])
print(myNewData)

print(myNewData.loc["India"])  # Accessing data for India


# Read csv file
df = pd.read_csv("pandas/data.csv")
print(df)



# Read json file
df_json = pd.read_json("pandas/data.json")
print(df_json)


print(df.head())       # Display the first 5 rows of the DataFrame
print(df.head(6))      # Display the first 6 rows
print(df.tail())        # Display the last 5 rows

print(df.info())