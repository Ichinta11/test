import pandas as pd
import numpy as np

# 1) Load raw
df = pd.read_csv("sales.csv")
print("Raw:\n", df)

# 2) Trim & normalize text columns
df["currency"] = df["currency"].astype(str).str.strip().str.upper()
df["customer"] = df["customer"].astype(str).str.strip()

# 3) amount -> numeric (invalid -> NaN)
df["amount"] = pd.to_numeric(df["amount"], errors="coerce")

# 4) order_date -> datetime (multi-format, invalid -> NaN)
df["order_date"] = pd.to_datetime(
    df["order_date"], errors="coerce", infer_datetime_format=True
)

print("\nAfter type fixes:\n", df.dtypes, "\n", df)

# 5) Missing values overview
print("\nMissing counts:\n", df.isna().sum())

# 6) Impute/fill: amount -> median; order_date -> forward fill
median_amt = df["amount"].median()
df["amount"] = df["amount"].fillna(median_amt)
df["order_date"] = df["order_date"].fillna(method="ffill")

# 7) Optional: customer missing అయితే Unknown
df["customer"] = df["customer"].replace({"nan": np.nan})  # safety
df["customer"] = df["customer"].fillna("Unknown")

# 8) Drop exact duplicates
before = len(df)
df = df.drop_duplicates()
after = len(df)
print(f"\nDuplicates removed: {before - after}")

# 9) Derive month
df["order_month"] = df["order_date"].dt.to_period("M").astype(str)

print("\nCleaned data:\n", df)

# 10) Aggregations for quick QA
monthly = df.groupby(["order_month", "currency"], as_index=False)["amount"].agg(["count", "sum", "mean"]).reset_index()
print("\nMonthly metrics:\n", monthly)

# 11) Save cleaned file
df.to_csv("sales_clean.csv", index=False)
print("\nSaved -> sales_clean.csv")
df = df[df["amount"] > 0]
df = df[df["currency"].isin(["USD","EUR"])]
