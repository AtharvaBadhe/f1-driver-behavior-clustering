import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go
import plotly.express as px
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
import warnings
warnings.filterwarnings('ignore')

# Set page configuration
st.set_page_config(page_title="F1 Driver Behavior Dashboard", layout="wide")

# Title and description
st.title("🏎️ F1 Driver Behavior Clustering Dashboard (2023)")
st.markdown("""
This dashboard analyzes driver behavior for Max Verstappen, Charles Leclerc, and Fernando Alonso across Monaco, Monza, and Silverstone in 2023. 
Explore clusters (Smooth Drivers vs. Aggressive Brakers), track-specific adaptations, performance correlations, and raw telemetry data from Phase 1.
""")

# Define expected features from Phase 4, aligned with Phase 1 context
FEATURES = [
    'Throttle_Rate', 'Coasting_Pct', 'Speed_Variance', 'Brake_Freq_Per_Km',
    'High_Throttle_Pct', 'Brake_Duration_Per_Km', 'Avg_Speed_Std', 'DRS_Efficiency',
    'Avg_Throttle_S1', 'Avg_Throttle_S2', 'Avg_Throttle_S3',
    'Brake_Percentage_S1', 'Brake_Percentage_S2', 'Brake_Percentage_S3',
    'Speed_Std_S1', 'Speed_Std_S2', 'Speed_Std_S3'
]

# Load and preprocess data
@st.cache_data
def load_data():
    try:
        # Load features and clustering results
        features_df = pd.read_csv('data/features_2023.csv')
        clusters_df = pd.read_csv('data/clustering_results_2023.csv')
        
        # Validate required columns
        required_cols = ['Driver', 'Race'] + FEATURES
        missing_cols = [col for col in required_cols if col not in features_df.columns]
        if missing_cols:
            st.warning(f"Missing columns in features_2023.csv: {missing_cols}. Found: {list(features_df.columns)}. Continuing with available columns.")
            available_features = [col for col in FEATURES if col in features_df.columns]
            if not available_features:
                raise ValueError("No valid feature columns found in features_2023.csv.")
        else:
            available_features = FEATURES
        
        required_cluster_cols = ['Driver', 'Race', 'Cluster']
        missing_cluster_cols = [col for col in required_cluster_cols if col not in clusters_df.columns]
        if missing_cluster_cols:
            raise ValueError(f"Missing columns in clustering_results_2023.csv: {missing_cluster_cols}")
        
        # Merge data
        data = features_df.merge(clusters_df[['Driver', 'Race', 'Cluster']], on=['Driver', 'Race'], how='left')
        
        # Check for unmatched rows
        if data['Cluster'].isna().any():
            st.warning("Some rows in features_2023.csv could not be matched with clustering_results_2023.csv. Dropping unmatched rows.")
            data = data.dropna(subset=['Cluster'])
        
        # Simulate LapTime as in Phase 4
        np.random.seed(42)
        lap_times = pd.DataFrame({
            'Driver': data['Driver'],
            'Race': data['Race'],
            'LapTime': np.random.normal(90, 5, size=len(data))
        })
        data = data.merge(lap_times, on=['Driver', 'Race'], how='left')
        
        # Scale features for PCA
        scaler = StandardScaler()
        data_scaled = pd.DataFrame(scaler.fit_transform(data[available_features]), columns=available_features)
        data_scaled['Driver'] = data['Driver'].astype(str)
        data_scaled['Race'] = data['Race'].astype(str)
        data_scaled['Cluster'] = data['Cluster']
        data_scaled['LapTime'] = data['LapTime']
        
        # Load telemetry data from Phase 1
        telemetry_data = pd.DataFrame()
        try:
            telemetry_data = pd.read_csv('data/combined_telemetry_2023.csv')
            expected_telemetry_cols = ['Distance', 'Speed', 'Throttle', 'Brake', 'RPM', 'DRS', 'Race', 'Driver', 'LapNumber']
            missing_telemetry_cols = [col for col in expected_telemetry_cols if col not in telemetry_data.columns]
            if missing_telemetry_cols:
                st.warning(f"combined_telemetry_2023.csv is missing expected columns: {missing_telemetry_cols}. Found: {list(telemetry_data.columns)}")
            # Ensure correct data types
            telemetry_data['Driver'] = telemetry_data['Driver'].astype(str)
            telemetry_data['Race'] = telemetry_data['Race'].astype(str)
            telemetry_data['LapNumber'] = pd.to_numeric(telemetry_data['LapNumber'], errors='coerce')
            telemetry_data['Distance'] = pd.to_numeric(telemetry_data['Distance'], errors='coerce')
            telemetry_data['Speed'] = pd.to_numeric(telemetry_data['Speed'], errors='coerce')
            telemetry_data['Throttle'] = pd.to_numeric(telemetry_data['Throttle'], errors='coerce')
            # Convert boolean Brake to numeric (True=1, False=0)
            if telemetry_data['Brake'].dtype == bool:
                telemetry_data['Brake'] = telemetry_data['Brake'].astype(int)
            telemetry_data['Brake'] = pd.to_numeric(telemetry_data['Brake'], errors='coerce')
            telemetry_data['RPM'] = pd.to_numeric(telemetry_data['RPM'], errors='coerce')
            telemetry_data['DRS'] = pd.to_numeric(telemetry_data['DRS'], errors='coerce')
            # Drop rows with NaN in critical columns
            telemetry_data = telemetry_data.dropna(subset=['Driver', 'Race', 'Distance', 'Speed', 'Throttle', 'Brake'])
        except FileNotFoundError:
            st.warning("combined_telemetry_2023.csv not found in data/. Telemetry visualization will be disabled.")
        except Exception as e:
            st.warning(f"Error loading combined_telemetry_2023.csv: {e}")
        
        return data, data_scaled, available_features, telemetry_data
    except FileNotFoundError as e:
        st.error(f"Data files not found: {e}. Ensure features_2023.csv and clustering_results_2023.csv are in data/.")
        return None, None, None, None
    except Exception as e:
        st.error(f"Unexpected error loading data: {e}")
        return None, None, None, None

data, data_scaled, features, telemetry_data = load_data()
if data is None:
    st.stop()

# Map cluster names
data['Cluster_Name'] = data['Cluster'].map({0: 'Smooth Drivers', 1: 'Aggressive Brakers'})

# Sidebar filters
st.sidebar.header("Filters")
driver_options = sorted(list(data['Driver'].unique())) if not data.empty else []
race_options = sorted(list(data['Race'].unique())) if not data.empty else []
cluster_options = ['Smooth Drivers (0)', 'Aggressive Brakers (1)']

# Ensure multiselect always returns a list
drivers = st.sidebar.multiselect("Select Driver(s)", options=driver_options, default=driver_options)
races = st.sidebar.multiselect("Select Race(s)", options=race_options, default=race_options)
clusters = st.sidebar.multiselect("Select Cluster(s)", options=cluster_options, default=cluster_options)

# Validate and normalize filters
drivers = list(drivers) if drivers else driver_options
races = list(races) if races else race_options
clusters = list(clusters) if clusters else cluster_options
cluster_names = [c.split(' (')[0] for c in clusters]

# Ensure string types for filters
drivers = [str(d) for d in drivers]
races = [str(r) for r in races]
cluster_names = [str(c) for c in cluster_names]

# Display filter warnings if defaults are used
if not drivers and driver_options:
    st.sidebar.warning("No drivers selected. Using all available drivers.")
if not races and race_options:
    st.sidebar.warning("No races selected. Using all available races.")
if not clusters and cluster_options:
    st.sidebar.warning("No clusters selected. Using all available clusters.")

# Filter data
filtered_data = data[
    data['Driver'].isin(list(drivers)) & 
    data['Race'].isin(list(races)) & 
    data['Cluster_Name'].isin(list(cluster_names))
]

# Layout
col1, col2 = st.columns(2)

# Radar Chart
with col1:
    st.subheader("Driver Profiles (Radar Chart)")
    radar_features = ['Throttle_Rate', 'Brake_Freq_Per_Km', 'DRS_Efficiency', 'High_Throttle_Pct', 'Avg_Speed_Std']
    radar_features = [f for f in radar_features if f in features]  # Use only available features
    if not filtered_data.empty and radar_features:
        fig = go.Figure()
        for race in sorted(filtered_data['Race'].unique()):
            race_data = filtered_data[filtered_data['Race'] == race]
            for driver in sorted(race_data['Driver'].unique()):
                values = (race_data[race_data['Driver'] == driver][radar_features].iloc[0] / 
                         data[radar_features].max() * 70).tolist()
                values += values[:1]  # Close the radar loop
                fig.add_trace(go.Scatterpolar(
                    r=values,
                    theta=radar_features + [radar_features[0]],
                    name=f"{driver} ({race})",
                    fill='toself',
                    opacity=0.3
                ))
        fig.update_layout(
            polar=dict(radialaxis=dict(visible=True, range=[0, 70])),
            showlegend=True,
            height=500,
            title="Driver Profiles for Selected Races"
        )
        st.plotly_chart(fig, use_container_width=True)
    else:
        st.warning("No data or valid features available for radar chart.")

# PCA Scatter Plot
with col2:
    st.subheader("Cluster Visualization (PCA)")
    if not filtered_data.empty and drivers and races and cluster_names and features:
        try:
            pca = PCA(n_components=2)
            pca_result = pca.fit_transform(data_scaled[features])
            pca_df = pd.DataFrame({
                'PC1': pca_result[:, 0],
                'PC2': pca_result[:, 1],
                'Driver': data['Driver'].astype(str),
                'Race': data['Race'].astype(str),
                'Cluster': data['Cluster_Name'],
                'LapTime': data['LapTime']
            })
            # Apply filters with explicit list conversion
            pca_df = pca_df[
                pca_df['Driver'].isin(list(drivers)) & 
                pca_df['Race'].isin(list(races)) & 
                pca_df['Cluster'].isin(list(cluster_names))
            ]
            if not pca_df.empty:
                fig = px.scatter(
                    pca_df, 
                    x='PC1', 
                    y='PC2', 
                    color='Cluster', 
                    symbol='Driver', 
                    size='LapTime',
                    hover_data=['Driver', 'Race'], 
                    title="PCA of Driver Behaviors by Cluster"
                )
                fig.update_traces(marker=dict(size=10, opacity=0.8))
                fig.update_layout(height=500)
                st.plotly_chart(fig, use_container_width=True)
            else:
                st.warning("No data matches the selected filters for PCA visualization.")
        except Exception as e:
            st.error(f"Error generating PCA plot: {e}")
    else:
        st.warning("No valid data or features selected for PCA visualization.")

# Box Plots
st.subheader("Key Features by Driver and Race")
key_features = ['Throttle_Rate', 'Brake_Freq_Per_Km', 'DRS_Efficiency']
key_features = [f for f in key_features if f in features]  # Use only available features
for feature in key_features:
    if not filtered_data.empty:
        fig = px.box(
            filtered_data, 
            x='Race', 
            y=feature, 
            color='Driver', 
            title=f"{feature} by Driver and Race"
        )
        fig.update_layout(height=400)
        st.plotly_chart(fig, use_container_width=True)
    else:
        st.warning(f"No data available for {feature} box plot.")

# Lap Time Distribution
st.subheader("Lap Time Distribution by Cluster")
if not filtered_data.empty:
    fig = px.box(
        filtered_data, 
        x='Cluster_Name', 
        y='LapTime', 
        color='Cluster_Name',
        title="Lap Time Distribution by Cluster"
    )
    fig.update_layout(height=400)
    st.plotly_chart(fig, use_container_width=True)
else:
    st.warning("No data available for lap time distribution.")

# Telemetry Visualization
with st.expander("📊 View Raw Telemetry Snapshot (Optional)"):
    st.markdown("Explore raw telemetry data from Phase 1 for selected drivers and races, showing Speed, Throttle, and Brake over Distance.")
    if not telemetry_data.empty:
        filtered_telemetry = telemetry_data[
            telemetry_data['Driver'].isin(list(drivers)) & 
            telemetry_data['Race'].isin(list(races))
        ]
        if not filtered_telemetry.empty:
            for driver in sorted(filtered_telemetry['Driver'].unique()):
                for race in sorted(filtered_telemetry['Race'].unique()):
                    driver_race_data = filtered_telemetry[
                        (filtered_telemetry['Driver'] == driver) & 
                        (filtered_telemetry['Race'] == race)
                    ]
                    if not driver_race_data.empty:
                        fig = go.Figure()
                        for metric in ['Speed', 'Throttle', 'Brake']:
                            if metric in driver_race_data.columns:
                                fig.add_trace(go.Scatter(
                                    x=driver_race_data['Distance'],
                                    y=driver_race_data[metric],
                                    mode='lines',
                                    name=f"{metric} ({driver}, {race})"
                                ))
                        fig.update_layout(
                            title=f"Telemetry: {driver} at {race} (Lap {driver_race_data['LapNumber'].iloc[0]})",
                            xaxis_title="Distance (km)",
                            yaxis_title="Value",
                            height=500,
                            showlegend=True
                        )
                        st.plotly_chart(fig, use_container_width=True)
                    else:
                        st.warning(f"No telemetry data for {driver} at {race}.")
            # Display sample telemetry data
            st.subheader("Sample Telemetry Data")
            display_cols = ['Driver', 'Race', 'LapNumber', 'Distance', 'Speed', 'Throttle', 'Brake']
            st.dataframe(filtered_telemetry[display_cols])
        else:
            st.warning("No telemetry data matches the selected filters.")
    else:
        st.warning("Telemetry data not available. Ensure combined_telemetry_2023.csv is in data/.")

# Recommendations with Tabs
st.subheader("Track-Specific Recommendations")
tab1, tab2 = st.tabs(["🟩 Smooth Drivers", "🟥 Aggressive Brakers"])
recommendations = {
    'Smooth Drivers': [
        'Maintain smooth throttle application in tight corners (e.g., Monaco’s hairpins).',
        'Optimize DRS usage in high-speed straights (e.g., Silverstone’s Hangar Straight).'
    ],
    'Aggressive Brakers': [
        'Reduce throttle aggression in S1 to improve tire wear.',
        'Minimize late braking in high-speed corners (e.g., Monza’s Parabolica).'
    ]
}

with tab1:
    if 'Smooth Drivers' in filtered_data['Cluster_Name'].unique():
        st.markdown("### 🟩 Smooth Drivers Recommendations")
        for rec in recommendations['Smooth Drivers']:
            st.markdown(f"- {rec}")
    else:
        st.info("No Smooth Drivers selected in current filters.")

with tab2:
    if 'Aggressive Brakers' in filtered_data['Cluster_Name'].unique():
        st.markdown("### 🟥 Aggressive Brakers Recommendations")
        for rec in recommendations['Aggressive Brakers']:
            st.markdown(f"- {rec}")
    else:
        st.info("No Aggressive Brakers selected in current filters.")

# Cluster Assignments Table
st.subheader("Cluster Assignments")
if not filtered_data.empty:
    cluster_pivot = filtered_data.pivot_table(
        index='Driver', 
        columns='Race', 
        values='Cluster_Name', 
        aggfunc='first'
    ).fillna('N/A')
    st.dataframe(cluster_pivot)
else:
    st.warning("No data available for cluster assignments.")

# Feature Data Table
st.subheader("Filtered Feature Data")
if not filtered_data.empty:
    display_cols = ['Driver', 'Race', 'Cluster_Name', 'LapTime'] + radar_features
    display_cols = [c for c in display_cols if c in data.columns]  # Ensure only available columns
    st.dataframe(filtered_data[display_cols])
else:
    st.warning("No data available for feature data table.")

# Footer
st.markdown("---")
st.markdown("Built by [Atharva Badhe](https://github.com/AtharvaBadhe)")
