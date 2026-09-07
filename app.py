import streamlit as st
import pandas as pd

# Page configuration
st.set_page_config(
    page_title="Smart Patient Vital-Sign Anomaly Detector",
    page_icon="🫀",
    layout="wide"
)

# Title
st.title("🫀 Smart Patient Vital-Sign Anomaly Detector")

st.write(
    "An educational biomedical AI prototype for detecting "
    "unusual patterns in patient vital-sign time-series data."
)

# Load processed data
data_file = "case_2168_anomaly_results.csv"

df = pd.read_csv(data_file)

st.success("Patient data loaded successfully!")

st.subheader("Dataset Overview")

st.write("Number of observations:", len(df))
st.write("Number of variables:", len(df.columns))

st.dataframe(df.head(10))
