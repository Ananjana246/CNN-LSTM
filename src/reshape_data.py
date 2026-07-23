import numpy as np

print("=" * 60)
print("RESHAPING DATA FOR CNN-LSTM")
print("=" * 60)

# Load processed datasets
X_train = np.load("dataset/processed/X_train.npy")
X_test = np.load("dataset/processed/X_test.npy")

print("\nOriginal Shapes")
print("X_train:", X_train.shape)
print("X_test :", X_test.shape)

# Reshape
X_train = X_train.reshape(
    X_train.shape[0],
    X_train.shape[1],
    1
)

X_test = X_test.reshape(
    X_test.shape[0],
    X_test.shape[1],
    1
)

print("\nReshaped Shapes")
print("X_train:", X_train.shape)
print("X_test :", X_test.shape)

# Save reshaped arrays
np.save(
    "dataset/processed/X_train_reshaped.npy",
    X_train
)

np.save(
    "dataset/processed/X_test_reshaped.npy",
    X_test
)

print("\n✅ Reshaped data saved successfully!")