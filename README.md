# 🏎️ F1 Driver Behavior Clustering (2023 Season Analysis)

[![Streamlit App](https://img.shields.io/badge/Live-Dashboard-0099ff?logo=streamlit)](https://f1-driver-behavior-clustering-vjf8dmpwzoheuk4dwpm5hl.streamlit.app/)
[![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)](https://www.python.org/)
[![License](https://img.shields.io/badge/license-MIT-green)](LICENSE)

## 🚀 Overview

This project analyzes **F1 driver behavioral patterns** using telemetry data from the **2023 season** (Monaco, Monza, Silverstone) for drivers like **Max Verstappen**, **Charles Leclerc**, and **Fernando Alonso**.

Using clustering and domain-specific features derived from telemetry, the drivers were grouped into **"Smooth Drivers"** and **"Aggressive Brakers"**, uncovering how behavior shifts with track layouts and correlates with performance (Lap Time, DRS usage, etc.).

A live **Streamlit dashboard** presents these insights interactively.

🔗 **Live App**: [F1 Driver Behavior Clustering Dashboard](https://f1-driver-behavior-clustering-vjf8dmpwzoheuk4dwpm5hl.streamlit.app/)

---

## 🎯 Problem Statement

> Can we identify patterns in driver behavior using telemetry data, and cluster them into meaningful driving styles?  
> How do these styles vary by track, and what performance tradeoffs do they imply?

---

## 📌 Project Phases

| Phase | Description |
|-------|-------------|
| **1. Exploratory Analysis** | Analyzed raw telemetry for Speed, Throttle, Brake, DRS, etc. |
| **2. Feature Engineering** | Created segment-wise (S1/S2/S3) and holistic features (e.g. `Throttle_Rate`, `Brake_Freq_Per_Km`). |
| **3. Clustering** | Applied KMeans and silhouette scoring to derive optimal driver behavior clusters. |
| **4. Interpretation** | Interpreted clusters using feature distributions and correlated them with simulated Lap Time. |
| **5. Dashboard (Final)** | Built a dynamic Streamlit app to explore behaviors, clusters, and recommendations.

---

## 🧠 Key Insights

- **Two dominant clusters** emerged:  
  - **Smooth Drivers** – High throttle control, stable speed.
  - **Aggressive Brakers** – High braking frequency, speed variance.
  
- Monaco favors smoother throttle modulation, while Monza rewards high-speed DRS efficiency.

- Aggressive behavior often correlates with **increased lap times** under certain track conditions.

---

## 📊 Dashboard Features

- **Radar Plots**: Compare driver profiles across races.
- **PCA Scatter**: Visualize driver clusters in 2D.
- **Box Plots**: Track-wise comparison of key features.
- **Lap Time Distributions**: Cluster-based performance comparison.
- **Telemetry Explorer**: Raw speed/throttle/brake trends per driver/lap.
- **Actionable Recommendations**: Cluster-specific driving suggestions.
- **Cluster Assignment Table**: Who drove how, and where.

> 📍 Try it yourself → [Live Streamlit App](https://f1-driver-behavior-clustering-vjf8dmpwzoheuk4dwpm5hl.streamlit.app/)

---

## 🧰 Tech Stack

- **Python 3.10+**
- `pandas`, `numpy`, `scikit-learn`, `plotly`, `streamlit`
- Data source: Processed telemetry (from FastF1 toolkit, pre-extracted CSV)

---

## 📸 Demo Screenshots

### Dashboard Overview
![Dashboard Overview]([assets/dashboard-overview.png](https://private-user-images.githubusercontent.com/151429414/457443092-f4eb60ea-4a3a-4cc9-ac36-2a6854a0974e.png?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3NTA0Mzc4NjMsIm5iZiI6MTc1MDQzNzU2MywicGF0aCI6Ii8xNTE0Mjk0MTQvNDU3NDQzMDkyLWY0ZWI2MGVhLTRhM2EtNGNjOS1hYzM2LTJhNjg1NGEwOTc0ZS5wbmc_WC1BbXotQWxnb3JpdGhtPUFXUzQtSE1BQy1TSEEyNTYmWC1BbXotQ3JlZGVudGlhbD1BS0lBVkNPRFlMU0E1M1BRSzRaQSUyRjIwMjUwNjIwJTJGdXMtZWFzdC0xJTJGczMlMkZhd3M0X3JlcXVlc3QmWC1BbXotRGF0ZT0yMDI1MDYyMFQxNjM5MjNaJlgtQW16LUV4cGlyZXM9MzAwJlgtQW16LVNpZ25hdHVyZT0zMjg2NjQxYjVhYmUyNjM0NjllNzcwMjU3ODdkYzUzMDEwYjI0ZDEwNTkxOTNhYTE5NTZjNjlmN2FhNTk4ZTZkJlgtQW16LVNpZ25lZEhlYWRlcnM9aG9zdCJ9.xWPPZjA5RSN8ie7jPgExKlVEtN8rEBLjI-GOoe9R5BM))

### Raw Telemetry Data
![Raw Data View](assets/raw-telemetry-data.png)

### Cluster Analysis Results
![Cluster Assignments](assets/cluster-assignments.png)

---

## 🛠️ How to Run Locally

```bash
# Clone the repository
git clone https://github.com/AtharvaBadhe/f1-driver-behavior-clustering.git
cd f1-driver-behavior-clustering

# Install dependencies
pip install -r requirements.txt

# Launch Streamlit app
streamlit run app.py

```
## 👨‍💻 Author

**Atharva Badhe**
- GitHub: [@your-github-username]((https://github.com/AtharvaBadhe))
- LinkedIn: [Your LinkedIn Profile]((https://www.linkedin.com/in/atharva-badhe/))
- Email: atharva.r.badhe@gmail.com

---

Made by Atharva Badhe
