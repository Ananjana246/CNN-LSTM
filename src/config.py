"""
Configuration File
CNN-LSTM IDS Project
"""

# Training Parameters
EPOCHS = 10
BATCH_SIZE = 32

# Optimizer
LEARNING_RATE = 0.001

# Dataset Paths
X_TRAIN = "dataset/processed/X_train_reshaped.npy"
X_TEST = "dataset/processed/X_test_reshaped.npy"

Y_TRAIN = "dataset/processed/y_train.npy"
Y_TEST = "dataset/processed/y_test.npy"

# Model Save Path
MODEL_PATH = "models/cnn_lstm.keras"