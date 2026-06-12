import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(
    page_title="Sales Analytics Dashboard",
    layout="wide"
)

st.title("Sales Analytics Dashboard")

# Load Data
df = pd.read_csv("sales.csv")

# Show Dataset
st.subheader("Dataset Preview")
st.dataframe(df)

# KPIs
total_sales = df["Sales"].sum()
avg_sales = df["Sales"].mean()
highest_sale = df["Sales"].max()

col1, col2, col3 = st.columns(3)

with col1:
    st.metric(
        "Total Revenue",
        f"${total_sales}"
    )

with col2:
    st.metric(
        "Average Sale",
        f"${avg_sales:.2f}"
    )

with col3:
    st.metric(
        "Highest Sale",
        f"${highest_sale}"
    )

# Revenue by Category
st.subheader("Revenue by Category")

category_sales = (
    df.groupby("Category")["Sales"]
    .sum()
)

fig, ax = plt.subplots()

category_sales.plot(
    kind="bar",
    ax=ax
)

ax.set_ylabel("Revenue")

st.pyplot(fig)

# Revenue by Region
st.subheader("Revenue by Region")

region_sales = (
    df.groupby("Region")["Sales"]
    .sum()
)

fig2, ax2 = plt.subplots()

region_sales.plot(
    kind="pie",
    autopct="%1.1f%%",
    ax=ax2
)

ax2.set_ylabel("")

st.pyplot(fig2)

# Top Products
st.subheader("Top Selling Products")

top_products = df.sort_values(
    by="Sales",
    ascending=False
)

st.dataframe(top_products)