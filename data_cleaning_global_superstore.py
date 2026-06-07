"""
SkillCraft Technology — Task 02
Data Cleaning and Preparation: Global Superstore
"""

import pandas as pd

# ─────────────────────────────────────────────
# 1. LOAD DATASET
# ─────────────────────────────────────────────
df = pd.read_csv("Global_Superstore2.csv", encoding="latin1", low_memory=False)

print("=" * 55)
print("STEP 1 — DATASET LOADED")
print("=" * 55)
print(f"Shape      : {df.shape[0]:,} rows × {df.shape[1]} columns")
print(f"Columns    : {list(df.columns)}\n")

# ─────────────────────────────────────────────
# 2. IDENTIFY MISSING VALUES
# ─────────────────────────────────────────────
print("=" * 55)
print("STEP 2 — MISSING VALUES (before cleaning)")
print("=" * 55)
missing = df.isnull().sum()
print(missing[missing > 0].to_string())
print()

# ─────────────────────────────────────────────
# 3. HANDLE MISSING VALUES
#    Postal Code is missing for ~80 % of rows
#    (most countries don't use postal codes).
#    Fill with 'N/A' so the column stays useful.
# ─────────────────────────────────────────────
df["Postal Code"] = df["Postal Code"].fillna("N/A")

print("=" * 55)
print("STEP 3 — MISSING VALUES (after cleaning)")
print("=" * 55)
missing_after = df.isnull().sum()
remaining = missing_after[missing_after > 0]
if remaining.empty:
    print("No missing values remain.\n")
else:
    print(remaining.to_string(), "\n")

# ─────────────────────────────────────────────
# 4. DROP DUPLICATE ROWS
# ─────────────────────────────────────────────
print("=" * 55)
print("STEP 4 — DUPLICATE ROWS")
print("=" * 55)
before = len(df)
df = df.drop_duplicates()
after = len(df)
print(f"Rows before : {before:,}")
print(f"Rows after  : {after:,}")
print(f"Removed     : {before - after:,} duplicate rows\n")

# ─────────────────────────────────────────────
# 5. CONVERT DATA TYPES
#    a) Order Date & Ship Date → datetime
#    b) Row ID & Quantity     → int
#    c) Postal Code           → str  (already done above)
# ─────────────────────────────────────────────
print("=" * 55)
print("STEP 5 — DATA TYPE CONVERSIONS")
print("=" * 55)

# Date columns (day-first format: 31-07-2012)
df["Order Date"] = pd.to_datetime(df["Order Date"], dayfirst=True)
df["Ship Date"]  = pd.to_datetime(df["Ship Date"],  dayfirst=True)

# Ensure numeric columns have correct types
df["Row ID"]   = df["Row ID"].astype(int)
df["Quantity"] = df["Quantity"].astype(int)

print("Updated dtypes:")
print(df[["Order Date", "Ship Date", "Row ID", "Quantity", "Postal Code"]].dtypes.to_string())
print()
print("Sample Order Date values after conversion:")
print(df["Order Date"].head(3).to_string(), "\n")

# ─────────────────────────────────────────────
# 6. FINAL SUMMARY
# ─────────────────────────────────────────────
print("=" * 55)
print("STEP 6 — FINAL DATASET SUMMARY")
print("=" * 55)
print(f"Shape      : {df.shape[0]:,} rows × {df.shape[1]} columns")
print(f"Missing    : {df.isnull().sum().sum()} total null values")
print(f"Duplicates : {df.duplicated().sum()}")
print()
print("All column dtypes:")
print(df.dtypes.to_string(), "\n")

# ─────────────────────────────────────────────
# 7. EXPORT CLEANED DATA
#    Dates are saved in ISO format (YYYY-MM-DD).
#    When re-loading, use parse_dates=['Order Date','Ship Date']
#    to restore datetime dtype automatically.
# ─────────────────────────────────────────────
output_path = "Cleaned_Global_Superstore.csv"
df.to_csv(output_path, index=False, date_format="%Y-%m-%d")

print("=" * 55)
print("STEP 7 — EXPORT COMPLETE")
print("=" * 55)
print(f"Saved to   : {output_path}")
print()
print("TIP: Re-load with datetime parsing using:")
print("  pd.read_csv('Cleaned_Global_Superstore.csv',")
print("              parse_dates=['Order Date', 'Ship Date'])")
