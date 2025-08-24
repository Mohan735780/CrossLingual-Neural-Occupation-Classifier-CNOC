#!/usr/bin/env python3
"""
Clean and normalize NAT scraped data for CNOC pipeline.

Input : raw/nat_all.csv
Output: interim/nat_clean.csv + interim/nat_clean.parquet
"""

import pandas as pd
from pathlib import Path
import re

RAW = Path("raw")
INTERIM = Path("interim"); INTERIM.mkdir(parents=True, exist_ok=True)

def normalize(df: pd.DataFrame) -> pd.DataFrame:
    # Drop rows missing essential fields
    df = df.dropna(subset=["nco_2015", "title"])

    # Clean serial number
    df["sno"] = pd.to_numeric(df["sno"], errors="coerce")

    # Normalize text fields
    for c in ["title", "division", "sub_division", "group", "family"]:
        df[c] = (
            df[c]
            .astype(str)
            .str.strip()
            .str.replace(r"\s+", " ", regex=True)  # collapse multiple spaces
        )

    # Normalize codes
    for c in ["nco_2015", "nco_2004"]:
        df[c] = df[c].astype(str).str.strip()

    # Drop duplicates
    df = df.drop_duplicates(subset=["nco_2015", "title"]).reset_index(drop=True)

    # Optional: enforce NCO code format ####.####
    def fix_code(code: str):
        if re.match(r"^\d{4}\.\d{2,4}$", code):
            return code
        return code  # leave unchanged if pattern unknown
    df["nco_2015"] = df["nco_2015"].map(fix_code)

    return df

def main():
    df = pd.read_csv(RAW / "nat_all.csv", dtype=str)
    print(f"Loaded {len(df)} raw rows")
    df = normalize(df)
    print(f"→ {len(df)} rows after cleaning")

    # Save clean versions
    df.to_csv(INTERIM / "nat_clean.csv", index=False)
    df.to_parquet(INTERIM / "nat_clean.parquet", index=False)
    print("✅ Clean dataset saved at interim/")

if __name__ == "__main__":
    main()
