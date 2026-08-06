import pandas as pd
from sklearn.linear_model import LinearRegression

data = {
    "experience": [1,2,3,4,5],
    "salary": [28000, 40000, 60000, 80000, 95000]
}

df = pd.DataFrame(data)

x = df[["experience"]]
y = df["salary"]

model = LinearRegression()
model.fit(x,y)

years = int(input("Enter years of experience: "))
new_experience = [[years]]

prediction = model.predict(new_experience)

print("Predicted Salary: ",prediction[0])
