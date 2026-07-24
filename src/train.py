import numpy as np

from model import build_model
import config
import pickle

# ----------------------------
# Load Dataset
# ----------------------------

print("=" * 60)
print("LOADING DATA")
print("=" * 60)

X_train = np.load(config.X_TRAIN)
X_test = np.load(config.X_TEST)

y_train = np.load(config.Y_TRAIN)
y_test = np.load(config.Y_TEST)

print("Training Shape :", X_train.shape)
print("Testing Shape  :", X_test.shape)

# ----------------------------
# Build Model
# ----------------------------

print("\nBuilding CNN-LSTM Model...\n")

model = build_model()

# ----------------------------
# Train Model
# ----------------------------

history = model.fit(
    X_train,
    y_train,
    epochs=config.EPOCHS,
    batch_size=config.BATCH_SIZE,
    validation_data=(X_test, y_test),
    verbose=1
)

with open("results/history.pkl", "wb") as f:
    pickle.dump(history.history, f)

print("✅ Training history saved!")

import pickle

# Save training history
with open("results/history.pkl", "wb") as file:
    pickle.dump(history.history, file)

print("✅ Training history saved successfully!")

# ----------------------------
# Save Model
# ----------------------------

model.save(config.MODEL_PATH)

print("\n✅ Model saved successfully!")