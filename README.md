# SCT_DA_2 — Data Cleaning and Preparation

**SkillCraft Technology | Data Analyst Internship | Task 02**

---

## 📌 Task Overview

Load the Global Superstore dataset into a Python environment using the Pandas library, perform data cleaning, and export the cleaned data to a new CSV file.

---

## 🎯 Objectives

- Identify and handle missing values
- Drop duplicate rows
- Convert data types (string columns to datetime format)
- Export the cleaned dataset to a new CSV file

---

## 📂 Repository Structure

```
SCT_DA_2/
│
├── data_cleaning_global_superstore.py   # Main cleaning script
├── Cleaned_Global_Superstore.csv        # Output: cleaned dataset
└── README.md                            # Project documentation
```

---

## 🗂️ Dataset

**Global Superstore** — a sample retail dataset containing international orders.

| Property | Value |
|----------|-------|
| Rows | 51,290 |
| Columns | 24 |
| Source | Global Superstore (sample retail data) |

**Key columns:** Row ID, Order ID, Order Date, Ship Date, Ship Mode, Customer Name, Segment, City, Country, Category, Sales, Quantity, Discount, Profit

---

## 🛠️ Tools & Libraries

| Tool | Purpose |
|------|---------|
| Python 3 | Programming language |
| Pandas | Data loading, cleaning, and export |

---

## 🧹 Cleaning Steps Performed

### 1. Load Dataset
```python
df = pd.read_csv("Global_Superstore2.csv", encoding="latin1", low_memory=False)
```

### 2. Identify Missing Values
- Found **41,296 missing values** in the `Postal Code` column
- Most countries in the dataset do not use postal codes

### 3. Handle Missing Values
```python
df["Postal Code"] = df["Postal Code"].fillna("N/A")
```
- Filled nulls with `"N/A"` to preserve all rows while flagging absence of data

### 4. Drop Duplicate Rows
```python
df = df.drop_duplicates()
```
- No duplicates were found in the original dataset (confirmed: 0 removed)

### 5. Convert Data Types
```python
df["Order Date"] = pd.to_datetime(df["Order Date"], dayfirst=True)
df["Ship Date"]  = pd.to_datetime(df["Ship Date"],  dayfirst=True)
df["Row ID"]     = df["Row ID"].astype(int)
df["Quantity"]   = df["Quantity"].astype(int)
```
- Dates converted from `DD-MM-YYYY` string format to `datetime64`
- Numeric columns enforced as `int64`

### 6. Export Cleaned Data
```python
df.to_csv("Cleaned_Global_Superstore.csv", index=False, date_format="%Y-%m-%d")
```

---

## ✅ Results Summary

| Check | Before | After |
|-------|--------|-------|
| Total rows | 51,290 | 51,290 |
| Missing values | 41,296 | 0 |
| Duplicate rows | 0 | 0 |
| Order Date dtype | object (string) | datetime64 |
| Ship Date dtype | object (string) | datetime64 |

---

## ▶️ How to Run

1. Clone this repository
2. Place `Global_Superstore2.csv` in the same folder
3. Run the script:
```bash
python data_cleaning_global_superstore.py
```
4. The cleaned file `Cleaned_Global_Superstore.csv` will be generated in the same directory

> **Note:** When re-loading the cleaned CSV, use `parse_dates=['Order Date', 'Ship Date']` to restore datetime dtypes automatically.

---

## 📚 Key Learnings

- Real-world datasets almost always require cleaning before analysis
- Strategy for handling missing data (fill vs. drop) depends on business context
- Proper data type management is critical for accurate downstream analysis
- Always validate the cleaned file against the original to catch unintended changes

---

*SkillCraft Technology — Data Analyst Internship*
