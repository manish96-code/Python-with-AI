import pandas as pd
from sklearn.linear_model import LogisticRegression

# 1. Simple Sample Dataset (Glucose, BMI, Age -> Diabetic: 1 = Yes, 0 = No)
data = {
    "glucose": [85, 120, 160, 95, 180, 105, 150, 90],
    "bmi": [22.0, 26.5, 32.0, 24.0, 35.5, 25.0, 30.0, 21.5],
    "age": [25, 45, 50, 30, 55, 35, 48, 28],
    "diabetic": [0, 0, 1, 0, 1, 0, 1, 0]
}

df = pd.DataFrame(data)

# 2. Features (X) and Target (y)
feature_cols = ["glucose", "bmi", "age"]
X = df[feature_cols]
y = df["diabetic"]

# 3. Train Logistic Regression Model
model = LogisticRegression()
model.fit(X, y)

# 4. User Input for new patient
print("--- Diabetes Prediction Model ---")
glucose_input = float(input("Enter Glucose level: "))
bmi_input = float(input("Enter BMI: "))
age_input = float(input("Enter Age: "))

new_patient = pd.DataFrame([[glucose_input, bmi_input, age_input]], columns=feature_cols)

# 5. Predict
prediction = model.predict(new_patient)

if prediction[0] == 1:
    print("\nResult: Diabetic 🩺 (High Risk)")
else:
    print("\nResult: Non-Diabetic ✅ (Low Risk)")
