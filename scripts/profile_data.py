import pandas as pd
from pathlib import Path

RAW_DATA_PATH = Path("data/raw")

datasets = {}

for csv_file in RAW_DATA_PATH.rglob("*.csv"):
    df = pd.read_csv(csv_file)
    datasets[csv_file.stem.lower()] = df

    print("\n" + "=" * 80)
    print(csv_file.name)
    print("=" * 80)

    for column in df.columns:
        print(
            f"{column:35} "
            f"unique={df[column].nunique():8} "
            f"nulls={df[column].isnull().sum():8}"
        )