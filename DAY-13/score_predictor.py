import pandas as pd

from sklearn.model_selection import train_test_split

from sklearn.linear_model import LinearRegression

from sklearn.metrics import mean_absolute_error

df = pd.read_csv(
    "student_scores.csv"
)

X = df[["Hours"]]

y = df["Score"]

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

model = LinearRegression()

model.fit(
    X_train,
    y_train
)

predictions = model.predict(
    X_test
)

mae = mean_absolute_error(
    y_test,
    predictions
)

print(
    "Mean Absolute Error:",
    mae
)

hours = pd.DataFrame(
    {"Hours": [6]}
)

predicted_score = model.predict(hours)

print(
    f"Predicted Score for 6 hours: {predicted_score[0]:.2f}"
)