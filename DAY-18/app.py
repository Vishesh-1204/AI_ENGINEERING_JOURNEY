import streamlit as st
import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

# Page Configuration
st.set_page_config(
    page_title="Student Placement Predictor",
    layout="centered"
)

st.title("Student Placement Predictor")

# Load Dataset
df = pd.read_csv("placement_data.csv")

# Features and Target
X = df[["CGPA", "Communication", "Projects"]]
y = df["Placed"]

# Train-Test Split
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# Train Model
model = LogisticRegression()
model.fit(X_train, y_train)

# Accuracy
predictions = model.predict(X_test)
accuracy = accuracy_score(y_test, predictions)

st.subheader("Model Accuracy")
st.success(f"{accuracy*100:.2f}%")

st.divider()

st.subheader("Enter Student Details")

cgpa = st.slider(
    "CGPA",
    5.0,
    10.0,
    7.5,
    0.1
)

communication = st.slider(
    "Communication Skills (1-10)",
    1,
    10,
    7
)

projects = st.slider(
    "Projects Completed",
    0,
    10,
    3
)

if st.button("Predict Placement"):

    student = pd.DataFrame({
        "CGPA": [cgpa],
        "Communication": [communication],
        "Projects": [projects]
    })

    prediction = model.predict(student)

    probability = model.predict_proba(student)

    if prediction[0] == 1:
        st.success("Student is likely to be Placed")
    else:
        st.error("Student is unlikely to be Placed")

    st.write(
        f"Placement Probability: {probability[0][1]*100:.2f}%"
    )