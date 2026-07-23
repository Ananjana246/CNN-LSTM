import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
import numpy as np




# Load cleaned dataset
df = pd.read_csv("dataset/processed/cleaned_portscan.csv")

print("=" * 60)
print("FEATURE ENGINEERING")
print("=" * 60)

print("\nDataset Shape:")
print(df.shape)

print("\nFirst Five Rows:")
print(df.head())

# Separate Features and Labels

X = df.drop("Label", axis=1)

y = df["Label"]

print("\nFeature Matrix Shape:", X.shape)
print("Label Vector Shape:", y.shape)

# Feature Scaling

scaler = StandardScaler()

X_scaled = scaler.fit_transform(X)

print("\nFeature Scaling Completed!")

print("Scaled Feature Shape:", X_scaled.shape)

# Split the dataset

X_train, X_test, y_train, y_test = train_test_split(
    X_scaled,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)

print("\nTrain-Test Split Completed!")

print("Training Samples :", X_train.shape)
print("Testing Samples  :", X_test.shape)

# Save the Processed Data

np.save("dataset/processed/X_train.npy", X_train)
np.save("dataset/processed/X_test.npy", X_test)

np.save("dataset/processed/y_train.npy", y_train)
np.save("dataset/processed/y_test.npy", y_test)

print("\n✅ Processed datasets saved successfully!")