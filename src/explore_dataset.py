import pandas as pd

# Path to the dataset
file_path = "dataset/raw/Friday-WorkingHours-Afternoon-PortScan.pcap_ISCX.csv"

# Load dataset
df = pd.read_csv(file_path)

print("Dataset Loaded Successfully!")
print()

# Shape of dataset
print("Shape of Dataset:")
print(df.shape)

print()

# Column names
print("Column Names:")
print(df.columns)

print()

# First five rows
print("First Five Rows:")
print(df.head())

print()

# Dataset information
print("Dataset Information:")
print(df.info())