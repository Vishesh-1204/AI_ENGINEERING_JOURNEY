from pathlib import Path

import joblib
import pandas as pd

from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split

BASE_DIR = Path(__file__).parent

csv_path = BASE_DIR / "placement_data.csv"

df = pd.read_csv(csv_path)

X = df[["CGPA", "Communication", "Projects"]]

y = df["Placed"]

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

model = LogisticRegression()

model.fit(
    X_train,
    y_train
)

model_path = BASE_DIR / "placement_model.pkl"

joblib.dump(
    model,
    model_path
)

print("Model saved successfully!")