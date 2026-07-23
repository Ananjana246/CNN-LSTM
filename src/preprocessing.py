import pandas as pd
import numpy as np

# Load dataset
file_path = "dataset/raw/Friday-WorkingHours-Afternoon-PortScan.pcap_ISCX.csv"
df = pd.read_csv(file_path)

print("=" * 60)
print("DATA PREPROCESSING")
print("=" * 60)

# Remove spaces
df.columns = df.columns.str.strip()

# Check for infinite values
print("\nChecking Infinite Values...")

inf_count = np.isinf(df.select_dtypes(include=[np.number])).sum().sum()

print("Total Infinite Values:", inf_count)

# Replace Infinity with NaN
df.replace([np.inf, -np.inf], np.nan, inplace=True)

# Check missing values
print("\nMissing Values:")
print(df.isnull().sum().sort_values(ascending=False).head(10))

# Remove missing values
df.dropna(inplace=True)

# Remove duplicate rows
before = df.shape[0]
df.drop_duplicates(inplace=True)
after = df.shape[0]

print("\nRows Before:", before)
print("Rows After :", after)
print("Duplicates Removed:", before - after)
print("\nFinal Shape:")

print(df.shape)

print("\nLabel Distribution:")
print(df["Label"].value_counts())

# Label Encoding
print("\nEncoding Labels...")

df["Label"] = df["Label"].map({
    "BENIGN": 0,
    "PortScan": 1
})
print("\nEncoded Label Distribution:")
print(df["Label"].value_counts())

# Save cleaned dataset
df.to_csv(
    "dataset/processed/cleaned_portscan.csv",
    index=False
)
print("\nCleaned dataset saved successfully!")