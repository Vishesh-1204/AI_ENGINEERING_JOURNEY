from pathlib import Path

import joblib
import pandas as pd
import streamlit as st

BASE_DIR = Path(__file__).parent

model = joblib.load(
    BASE_DIR / "placement_model.pkl"
)

st.set_page_config(
    page_title="Student Placement Predictor",
    layout="centered"
)

st.title("Student Placement Predictor")

st.write(
    "Predict whether a student is likely to be placed based on academic performance."
)

cgpa = st.slider(
    "CGPA",
    5.0,
    10.0,
    7.5,
    0.1
)

communication = st.slider(
    "Communication Skills",
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

    st.divider()

    if prediction[0] == 1:

        st.success(
            "Student is likely to be Placed"
        )

    else:

        st.error(
            "Student is unlikely to be Placed"
        )

    st.metric(
        "Placement Probability",
        f"{probability[0][1]*100:.2f}%"
    )