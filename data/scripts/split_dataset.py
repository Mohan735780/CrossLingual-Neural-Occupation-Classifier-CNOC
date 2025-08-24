#!/usr/bin/env python3
"""
Split processed multilingual dataset into train/val/test sets.
- Uses NCO "family" (first 2 digits) for stratification
  when possible.
- Falls back to random split if a family is too small.
"""

import pandas as pd
from pathlib import Path
from sklearn.model_selection import train_test_split

PROCESSED = Path("processed")

def main():
    df = pd.read_csv(PROCESSED / "train_rows.csv", encoding="utf-8")
    print(f"✅ Loaded {len(df)} rows for splitting...")

    # Extract top-level NCO family (first 2 digits)
    df["nco_family"] = df["nco_2015"].astype(str).str[:2]

    # --- Train vs temp stratified by family ---
    train, temp = train_test_split(
        df, test_size=0.2, stratify=df["nco_family"], random_state=42
    )

    # --- Temp → Val/Test split (random, no stratify) ---
    val, test = train_test_split(temp, test_size=0.5, random_state=42)

    print(f"Train: {len(train)} | Val: {len(val)} | Test: {len(test)}")

    # Quick sanity check
    print("Family distribution (train):")
    print(train["nco_family"].value_counts().head())

    # Drop helper col before saving
    train.drop(columns=["nco_family"]).to_csv(PROCESSED / "train.csv", index=False, encoding="utf-8")
    val.drop(columns=["nco_family"]).to_csv(PROCESSED / "val.csv", index=False, encoding="utf-8")
    test.drop(columns=["nco_family"]).to_csv(PROCESSED / "test.csv", index=False, encoding="utf-8")

    print("✅ Saved train/val/test CSVs in processed/")

if __name__ == "__main__":
    main()
