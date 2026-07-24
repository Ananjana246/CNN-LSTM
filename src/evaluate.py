import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os
from sklearn.metrics import roc_curve, auc

from tensorflow.keras.models import load_model

from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    confusion_matrix,
    classification_report
)

import config

print("=" * 60)
print("MODEL EVALUATION")
print("=" * 60)

# ------------------------
# Load Model
# ------------------------

model = load_model(config.MODEL_PATH)

print("\n✅ Model Loaded Successfully!")

# ------------------------
# Load Test Data
# ------------------------

X_test = np.load(config.X_TEST)
y_test = np.load(config.Y_TEST)

# ------------------------
# Predictions
# ------------------------

y_prob = model.predict(X_test)

# Convert probabilities to 0 or 1

y_pred = (y_prob > 0.5).astype(int)

# ------------------------
# Metrics
# ------------------------

accuracy = accuracy_score(y_test, y_pred)
precision = precision_score(y_test, y_pred)
recall = recall_score(y_test, y_pred)
f1 = f1_score(y_test, y_pred)

print("\nAccuracy :", accuracy)
print("Precision:", precision)
print("Recall   :", recall)
print("F1 Score :", f1)

# ------------------------
# Confusion Matrix
# ------------------------

cm = confusion_matrix(y_test, y_pred)

print("\nConfusion Matrix")

print(cm)

# ------------------------
# Confusion Matrix Heatmap
# ------------------------

os.makedirs("results/plots", exist_ok=True)
plt.figure(figsize=(6,5))

sns.heatmap(
    cm,
    annot=True,
    fmt="d",
    cmap="Blues",
    xticklabels=["Normal", "Attack"],
    yticklabels=["Normal", "Attack"]
)

plt.title("Confusion Matrix")
plt.xlabel("Predicted Label")
plt.ylabel("True Label")

plt.tight_layout()
plt.savefig("results/plots/confusion_matrix.png")
plt.show()

print("✅ Confusion Matrix Heatmap Saved!")

# ------------------------
# ROC Curve
# ------------------------

fpr, tpr, _ = roc_curve(y_test, y_prob)
roc_auc = auc(fpr, tpr)

plt.figure(figsize=(6,6))
plt.plot(fpr, tpr,
         label=f"AUC = {roc_auc:.4f}",
         linewidth=2)

plt.plot([0,1],[0,1],'k--')
plt.xlabel("False Positive Rate")
plt.ylabel("True Positive Rate")
plt.title("ROC Curve")
plt.legend(loc="lower right")
plt.grid(True)
plt.tight_layout()
plt.savefig("results/plots/roc_curve.png")
plt.show()

print(f"ROC AUC Score: {roc_auc:.4f}")
print("✅ ROC Curve Saved!")

# ------------------------
# Classification Report
# ------------------------

print("\nClassification Report")

print(
    classification_report(
        y_test,
        y_pred,
        target_names=["Normal", "Attack"]
    )
)