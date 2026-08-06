import pandas as pd
from sklearn.linear_model import LinearRegression

data = {
    "size": [10,12,14,16],
    "price": [100,120,140,160]
}

df = pd.DataFrame(data)

X = df[["size"]]
y = df["price"]

model = LinearRegression()
model.fit(X,y)
new_size = [[13]]

prediction = model.predict(new_size)

print("Predicted Price: ",prediction[0])
print("Slope: ", model.coef_[0])
print("Intercept: ", model.intercept_)
print("Accuracy: ",model.score(X,y))