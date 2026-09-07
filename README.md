# Smart Patient Vital-Sign Anomaly Detector

##  Overview

A biomedical AI prototype that analyzes patient vital-sign time-series data and detects unusual deviations from a patient-specific baseline.

The project uses real-world perioperative physiological data from the VitalDB Open Dataset and focuses on Heart Rate (HR) and Oxygen Saturation (SpO₂).

> ⚠️ This project is intended for educational and research purposes. It is not a clinical diagnostic or decision-making system.

---

## Objectives

- Analyze real-world physiological time-series data.
- Handle missing and irregular biomedical measurements.
- Establish patient-specific vital-sign baselines.
- Detect unusual deviations using statistical methods.
- Assign anomaly severity levels.
- Visualize physiological trends through an interactive dashboard.

---

## Dataset

The project uses the **VitalDB Open Dataset**, which contains physiological and clinical data collected during surgical procedures.

### Vital signs used

| Signal | Description |
|---|---|
| Heart Rate (HR) | Beats per minute |
| SpO₂ | Peripheral oxygen saturation |

The main development case used in this project is **Case 2168**.

---

## Methodology

```text
VitalDB Dataset
       ↓
Data Loading
       ↓
Data Cleaning
       ↓
Missing-value Handling
       ↓
HR + SpO₂ Selection
       ↓
Patient-specific Rolling Baseline
       ↓
Deviation Calculation
       ↓
Anomaly Detection
       ↓
Severity Classification
       ↓
Interactive Dashboard
