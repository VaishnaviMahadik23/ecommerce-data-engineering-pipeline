import pandas as pd
from pathlib import Path

RAW_DATA_PATH = Path("data/raw")

for csv_file in RAW_DATA_PATH.rglob("*.csv"):

    print("\n" + "=" * 80)
    print(f"FILE: {csv_file}")
    print("=" * 80)

    df = pd.read_csv(csv_file)

    print(f"Rows    : {df.shape[0]}")
    print(f"Columns : {df.shape[1]}")

    print("\nColumns:")
    print(df.columns.tolist())

    print("\nData Types:")
    print(df.dtypes)

    print("\nMissing Values:")
    print(df.isnull().sum())

    print("\nDuplicate Rows:")
    print(df.duplicated().sum())

    print("\nFirst 5 Records:")
    print(df.head())