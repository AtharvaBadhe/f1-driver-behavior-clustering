import pandas as pd
import numpy as np
import os

# Create data directory if it doesn't exist
os.makedirs('../data', exist_ok=True)

# Define drivers and races
drivers = ['Max Verstappen', 'Charles Leclerc', 'Fernando Alonso']
races = ['Monaco', 'Monza', 'Silverstone']

# Define features from Phase 4
features = [
    'Throttle_Rate', 'Coasting_Pct', 'Speed_Variance', 'Brake_Freq_Per_Km',
    'High_Throttle_Pct', 'Brake_Duration_Per_Km', 'Avg_Speed_Std', 'DRS_Efficiency',
    'Avg_Throttle_S1', 'Avg_Throttle_S2', 'Avg_Throttle_S3',
    'Brake_Percentage_S1', 'Brake_Percentage_S2', 'Brake_Percentage_S3',
    'Speed_Std_S1', 'Speed_Std_S2', 'Speed_Std_S3'
]

# Generate sample features_2023.csv
np.random.seed(42)
feature_data = []
for driver in drivers:
    for race in races:
        row = {
            'Driver': driver,
            'Race': race
        }
        # Generate realistic feature values
        row['Throttle_Rate'] = np.random.uniform(0.5, 1.0)
        row['Coasting_Pct'] = np.random.uniform(10, 30)
        row['Speed_Variance'] = np.random.uniform(50, 100)
        row['Brake_Freq_Per_Km'] = np.random.uniform(3, 7)
        row['High_Throttle_Pct'] = np.random.uniform(20, 50)
        row['Brake_Duration_Per_Km'] = np.random.uniform(2, 5)
        row['Avg_Speed_Std'] = np.random.uniform(10, 20)
        row['DRS_Efficiency'] = np.random.uniform(5, 15)
        row['Avg_Throttle_S1'] = np.random.uniform(60, 90)
        row['Avg_Throttle_S2'] = np.random.uniform(60, 90)
        row['Avg_Throttle_S3'] = np.random.uniform(60, 90)
        row['Brake_Percentage_S1'] = np.random.uniform(10, 30)
        row['Brake_Percentage_S2'] = np.random.uniform(10, 30)
        row['Brake_Percentage_S3'] = np.random.uniform(10, 30)
        row['Speed_Std_S1'] = np.random.uniform(5, 15)
        row['Speed_Std_S2'] = np.random.uniform(5, 15)
        row['Speed_Std_S3'] = np.random.uniform(5, 15)
        feature_data.append(row)

features_df = pd.DataFrame(feature_data)
features_df.to_csv('../data/features_2023.csv', index=False)

# Generate sample clustering_results_2023.csv
cluster_data = []
for driver in drivers:
    for race in races:
        # Assign clusters based on Phase 4 example (simplified)
        cluster = 0 if driver in ['Max Verstappen', 'Fernando Alonso'] and race != 'Monza' else 1
        cluster_data.append({
            'Driver': driver,
            'Race': race,
            'Cluster': cluster
        })

clusters_df = pd.DataFrame(cluster_data)
clusters_df.to_csv('../data/clustering_results_2023.csv', index=False)

print("Sample data files created: ../data/features_2023.csv and ../data/clustering_results_2023.csv")