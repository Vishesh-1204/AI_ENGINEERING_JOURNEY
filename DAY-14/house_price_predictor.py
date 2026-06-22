import pandas as pd

from sklearn.model_selection import train_test_split

from sklearn.linear_model import LinearRegression

from sklearn.metrics import mean_absolute_error

df = pd.read_csv(
    "house_prices.csv"
)

X = df[["Size"]]

y = df["Price"]

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
    round(mae, 2)
)

new_house = pd.DataFrame(
    {"Size": [2300]}
)

predicted_price = model.predict(
    new_house
)

print(
    f"Predicted Price: ₹{predicted_price[0]:,.0f}"
)

import matplotlib.pyplot as plt

plt.scatter(
    X,
    y
)

plt.plot(
    X,
    model.predict(X)
)

plt.xlabel("House Size")
plt.ylabel("House Price")

plt.title(
    "House Price Prediction"
)

plt.show()