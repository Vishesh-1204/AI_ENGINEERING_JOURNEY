import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix

# Load Dataset
df = pd.read_csv("customer_churn.csv")

# Features
X = df[["Age", "MonthlyCharges"]]

# Target
y = df["Churn"]

# Split Dataset
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# Train Model
model = LogisticRegression()

model.fit(X_train, y_train)

# Predictions
predictions = model.predict(X_test)

# Accuracy
accuracy = accuracy_score(y_test, predictions)

print(f"Accuracy: {accuracy:.2f}")

# Confusion Matrix
print("\nConfusion Matrix:")
print(confusion_matrix(y_test, predictions))

# Predict New Customer
new_customer = pd.DataFrame({
    "Age": [33],
    "MonthlyCharges": [850]
})

prediction = model.predict(new_customer)

probability = model.predict_proba(new_customer)

if prediction[0] == 1:
    print("\nPrediction: Customer is likely to Churn")
else:
    print("\nPrediction: Customer is likely to Stay")

print(f"Probability of Churn: {probability[0][1]*100:.2f}%")