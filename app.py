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

# Dashboard metrics

total_observations = len(df)
anomaly_count = int(df["Anomaly"].sum())
anomaly_percentage = round(
    (anomaly_count / total_observations) * 100, 2
)
high_severity = int((df["Severity"] == "High").sum())

col1, col2, col3, col4 = st.columns(4)

col1.metric("Total Observations", total_observations)
col2.metric("Detected Anomalies", anomaly_count)
col3.metric("Anomaly Rate", f"{anomaly_percentage}%")
col4.metric("High Severity", high_severity)

st.subheader("Recent Patient Data")

st.dataframe(df.head(10), use_container_width=True)
