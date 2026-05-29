import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("/content/healthcare-dataset-stroke-data.csv")

st.title("Stroke Prediction EDA Dashboard")

st.write(df.head())

# Sidebar Filters
gender = st.sidebar.multiselect(
    "Select Gender",
    options=df['gender'].unique(),
    default=df['gender'].unique()
)

filtered_df = df[df['gender'].isin(gender)]

# Chart
fig, ax = plt.subplots(figsize=(8,5))

sns.countplot(
    x='gender',
    hue='stroke',
    data=filtered_df,
    ax=ax
)

st.pyplot(fig)
gender = st.sidebar.multiselect(...)
age_range = st.sidebar.slider(
    "Age Range",
    int(df.age.min()),
    int(df.age.max()),
    (20, 80)
)
smoking = st.sidebar.multiselect(
    "Select Smoking Status",
    options=df['smoking_status'].unique(),
    default=df['smoking_status'].unique()
)
filtered_df = filtered_df[filtered_df['age'].between(age_range[0], age_range[1])]
filtered_df = filtered_df[filtered_df['smoking_status'].isin(smoking)]
search = st.sidebar.text_input("Search")
st.sidebar.button("Reset Filters")
col1, col2, col3 = st.columns(3)

col1.metric("Total Records", len(df))
col2.metric("Average Age", round(df['age'].mean(),2))
col3.metric("Stroke Cases", df['stroke'].sum())