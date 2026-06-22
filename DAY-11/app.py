import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Messy Dataset Cleaner",
    layout="wide"
)

st.title(
    "Messy Dataset Cleaner"
)

uploaded_file = st.file_uploader(
    "Upload CSV File",
    type=["csv"]
)

if uploaded_file:

    df = pd.read_csv(uploaded_file)

    st.subheader("Original Dataset")

    st.dataframe(df)

    st.subheader("Dataset Information")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric(
            "Rows",
            df.shape[0]
        )

    with col2:
        st.metric(
            "Columns",
            df.shape[1]
        )

    with col3:
        st.metric(
            "Missing Values",
            df.isnull().sum().sum()
        )

    st.subheader("Missing Values Per Column")

    st.dataframe(
        df.isnull().sum()
    )

    cleaned_df = df.copy()

    # Remove duplicates
    cleaned_df = cleaned_df.drop_duplicates()

    # Fill missing values
    cleaned_df = cleaned_df.fillna(
        "Unknown"
    )

    st.subheader(
        "Cleaned Dataset"
    )

    st.dataframe(
        cleaned_df
    )

    csv = cleaned_df.to_csv(
        index=False
    )

    st.download_button(
        "Download Cleaned Dataset",
        csv,
        "cleaned_data.csv",
        "text/csv"
    )