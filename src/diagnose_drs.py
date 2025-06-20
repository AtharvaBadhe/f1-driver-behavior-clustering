#Well,while doing EDA we got DRS usage % 0, so just needed to check whether really it is or not
import pandas as pd
from pathlib import Path

def diagnose_drs(data_dir: str, drivers: list) -> None:
    """Load telemetry CSVs and check DRS values for each driver."""
    data_path = Path(data_dir)
    for driver in drivers:
        file_path = data_path / f"raw_telemetry_{driver}_monaco_2023.csv"
        if not file_path.exists():
            print(f"Error: Telemetry file for {driver} not found at {file_path}")
            continue
        
        # Load telemetry
        telemetry = pd.read_csv(file_path)
        
        # Check DRS column
        if 'DRS' not in telemetry.columns:
            print(f"Error: DRS column missing for {driver}")
            continue
        
        # Summarize DRS usage
        drs_values = telemetry['DRS']
        drs_usage_pct = (drs_values > 0).mean() * 100
        drs_unique = drs_values.unique()
        drs_non_zero_count = (drs_values > 0).sum()
        
        print(f"\nDRS Diagnostics for {driver}:")
        print(f"  Unique DRS values: {drs_unique}")
        print(f"  DRS Usage (% of lap): {drs_usage_pct:.2f}%")
        print(f"  Non-zero DRS points: {drs_non_zero_count}")
        print(f"  Total data points: {len(drs_values)}")

def main():
    """Main function to diagnose DRS values."""
    data_dir = "data"
    drivers = ['VER', 'LEC', 'ALO']
    diagnose_drs(data_dir, drivers)

if __name__ == "__main__":
    main()