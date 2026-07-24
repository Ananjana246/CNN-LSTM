import pickle
import matplotlib.pyplot as plt
import os

# Create plots folder if it doesn't exist
os.makedirs("results/plots", exist_ok=True)

# Load training history
with open("results/history.pkl", "rb") as file:
    history = pickle.load(file)

# -------------------------
# Accuracy Plot
# -------------------------

plt.figure(figsize=(8,5))

plt.plot(history["accuracy"], label="Training Accuracy")
plt.plot(history["val_accuracy"], label="Validation Accuracy")

plt.title("Model Accuracy")
plt.xlabel("Epoch")
plt.ylabel("Accuracy")
plt.legend()

plt.grid(True)
plt.savefig("results/plots/accuracy.png")
plt.show()

# -------------------------
# Loss Plot
# -------------------------

plt.figure(figsize=(8,5))
plt.plot(history["loss"], label="Training Loss")
plt.plot(history["val_loss"], label="Validation Loss")

plt.title("Model Loss")
plt.xlabel("Epoch")
plt.ylabel("Loss")
plt.legend()

plt.grid(True)
plt.savefig("results/plots/loss.png")
plt.show()

print("✅ Graphs saved successfully!")