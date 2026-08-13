import pandas as pd
from sklearn.linear_model import LogisticRegression


data = pd.read_csv("scikit/email.csv")

print(data)


# 1. Feature variables and Target variable
X = data[["free", "win", "offer", "meeting", "report", "money"]]
y = data["Prediction"]

# 2. Train Logistic Regression model
model = LogisticRegression()
model.fit(X, y)

# 3. New email data to check [free, win, offer, meeting, report, money]
# Example: 2 "free", 1 "win", 1 "offer", 0 "meeting", 0 "report", 1 "money"
feature_cols = ["free", "win", "offer", "meeting", "report", "money"]
new_email = pd.DataFrame([[2, 1, 1, 0, 0, 1]], columns=feature_cols)

# 4. Predict
prediction = model.predict(new_email)

if prediction[0] == 1:
    print("Spam Email 🚨")
else:
    print("Not Spam Email ✅")





