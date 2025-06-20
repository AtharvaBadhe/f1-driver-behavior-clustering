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
![Dashboard Overview](![Image](https://github.com/user-attachments/assets/f4eb60ea-4a3a-4cc9-ac36-2a6854a0974e)

### Raw Telemetry Data
![Raw Data View](![Image](https://github.com/user-attachments/assets/defdc249-ba90-4607-a06a-ae544dbcda8c))

### Cluster Analysis Results
![Cluster Assignments](![Image](https://github.com/user-attachments/assets/11617442-5ef9-4ac4-add9-f9a9c93970d1))

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
