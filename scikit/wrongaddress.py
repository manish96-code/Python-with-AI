import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.linear_model import LogisticRegression

# Dataset: Addresses with labels (1 = Spam/Fake Address, 0 = Valid Address)
data = {
    "address": [
        "123 MG Road, Sector 15, Gurgaon, Haryana",
        "asdfghj 00000 fake street xyz",
        "Flat 402, Sunshine Apartments, Bandra, Mumbai",
        "test test test test 12345",
        "House No 45, Park Street, Kolkata, West Bengal",
        "qwertyuiop 999999 null city",
        "742 Evergreen Terrace, Springfield, OR 97477",
        "x x x x x x x x x x",
        "Plot 12, Tech Park, Whitefield, Bengaluru",
        "fake address fake location 000"
    ],
    "is_spam": [0, 1, 0, 1, 0, 1, 0, 1, 0, 1]
}

df = pd.DataFrame(data)

# Convert raw address text into numerical feature matrix
cv = CountVectorizer()
X = cv.fit_transform(df["address"])
y = df["is_spam"]

# Train Logistic Regression model
model = LogisticRegression()
model.fit(X, y)

# User input for address verification
print("--- Address Spam / Fake Checker ---")
user_address = input("Enter an address to check: ")

# Transform user input and predict
user_vec = cv.transform([user_address])
prediction = model.predict(user_vec)

if prediction[0] == 1:
    print("\nResult: 🚨 Spam / Invalid Address Detected!")
else:
    print("\nResult: ✅ Valid Address!")
