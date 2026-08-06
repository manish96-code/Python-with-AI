import pandas as pd
from sklearn.linear_model import LinearRegression

data = {
    "area": [1000, 1500, 2000, 2500, 3000],
    "price": [100000, 200000, 300000, 400000, 500000]
}

df = pd.DataFrame(data)

x = df[["area"]]
y = df["price"]

model = LinearRegression()
model.fit(x, y)

user_area = float(input("Enter area: "))
new_area = [[user_area]]

prediction = model.predict(new_area)

print("Predicted Price: ",prediction[0])