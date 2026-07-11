import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

# Load Dataset
df = pd.read_csv("loan_data.csv")

# Features
X = df[["Income", "CreditScore"]]

# Target
y = df["Loan"]

# Split Data
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# Decision Tree Model
tree_model = DecisionTreeClassifier(
    random_state=42
)

tree_model.fit(X_train, y_train)

tree_predictions = tree_model.predict(X_test)

tree_accuracy = accuracy_score(
    y_test,
    tree_predictions
)

print(f"Decision Tree Accuracy: {tree_accuracy:.2f}")

# Random Forest Model
forest_model = RandomForestClassifier(
    n_estimators=100,
    random_state=42
)

forest_model.fit(X_train, y_train)

forest_predictions = forest_model.predict(X_test)

forest_accuracy = accuracy_score(
    y_test,
    forest_predictions
)

print(f"Random Forest Accuracy: {forest_accuracy:.2f}")

# Predict New Applicant
new_applicant = pd.DataFrame({
    "Income": [65000],
    "CreditScore": [740]
})

prediction = forest_model.predict(new_applicant)

if prediction[0] == 1:
    print("\nLoan Approved")
else:
    print("\nLoan Rejected")