import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(
    page_title="Interactive Analytics Dashboard",
    layout="wide"
)

st.title(
    "Interactive Analytics Dashboard"
)

uploaded_file = st.file_uploader(
    "Upload Sales CSV",
    type=["csv"]
)

if uploaded_file:

    df = pd.read_csv(uploaded_file)

    st.subheader(
        "Dataset Preview"
    )

    st.dataframe(df)

    total_sales = df["Sales"].sum()
    avg_sales = df["Sales"].mean()
    max_sales = df["Sales"].max()

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric(
            "Total Revenue",
            f"${total_sales}"
        )

    with col2:
        st.metric(
            "Average Sale",
            f"${avg_sales:.0f}"
        )

    with col3:
        st.metric(
            "Highest Sale",
            f"${max_sales}"
        )

    st.divider()

    st.subheader(
        "Revenue by Category"
    )

    category_sales = (
        df.groupby("Category")["Sales"]
        .sum()
        .reset_index()
    )

    fig1 = px.bar(
        category_sales,
        x="Category",
        y="Sales",
        title="Revenue by Category"
    )

    st.plotly_chart(
        fig1,
        use_container_width=True
    )

    st.subheader(
        "Revenue by Region"
    )

    region_sales = (
        df.groupby("Region")["Sales"]
        .sum()
        .reset_index()
    )

    fig2 = px.pie(
        region_sales,
        names="Region",
        values="Sales",
        title="Revenue by Region"
    )

    st.plotly_chart(
        fig2,
        use_container_width=True
    )

    st.subheader(
        "Top Products"
    )

    fig3 = px.bar(
        df.sort_values(
            by="Sales",
            ascending=False
        ),
        x="Product",
        y="Sales",
        title="Product Performance"
    )

    st.plotly_chart(
        fig3,
        use_container_width=True
    )