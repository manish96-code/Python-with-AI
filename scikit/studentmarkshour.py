import pandas as pd
from sklearn.linear_model import LinearRegression

data = {
    "study_hours": [4, 8, 10, 12, 14, 18, 20],
    "marks": [40, 48, 52, 55, 58, 62, 69]
}

df = pd.DataFrame(data)

x = df[["study_hours"]]
y = df["marks"]

model = LinearRegression()
model.fit(x,y)

hours = int(input("Enter study hours: "))
new_hours = [[hours]]

prediction = model.predict(new_hours)

print("Predicted Marks: ",prediction[0])
