# -*- coding: utf-8 -*-
"""AWS_LGBM.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1ExQh88aNpeS0Wqu145_t6DF_IoBNbm3t
"""

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.metrics import (
    accuracy_score, cohen_kappa_score, confusion_matrix,
    roc_curve, auc, precision_score, recall_score, f1_score
)
from lightgbm import LGBMClassifier
import numpy as np

# Load data
df = pd.read_csv("combined_fraud_dataset.csv")

# Drop rows with missing target
df = df.dropna(subset=['isFraud'])

# Now define Features and Target
X = df[['amount', 'source_encoded']]
y = df['isFraud']

# Train-test split
X_train, X_val, y_train, y_val = train_test_split(X, y, test_size=0.3, random_state=42, stratify=y)

# Initialize and train the model with balanced class weight
model = LGBMClassifier(random_state=42, class_weight='balanced')
model.fit(X_train, y_train)

# Predictions (probabilities)
y_val_proba = model.predict_proba(X_val)[:, 1]

# Find best threshold based on maximizing F1-Score
thresholds = np.arange(0.1, 0.9, 0.01)
f1_scores = []

for thresh in thresholds:
    y_thresh_pred = (y_val_proba >= thresh).astype(int)
    f1 = f1_score(y_val, y_thresh_pred)
    f1_scores.append(f1)

best_thresh = thresholds[np.argmax(f1_scores)]

# Final Predictions based on best threshold
y_train_pred = (model.predict_proba(X_train)[:, 1] >= best_thresh).astype(int)
y_val_pred = (y_val_proba >= best_thresh).astype(int)

# Accuracy
train_accuracy = accuracy_score(y_train, y_train_pred)
val_accuracy = accuracy_score(y_val, y_val_pred)

# Other metrics
precision = precision_score(y_val, y_val_pred)
recall = recall_score(y_val, y_val_pred)
f1 = f1_score(y_val, y_val_pred)
kappa = cohen_kappa_score(y_val, y_val_pred)

# Confusion Matrix
cm = confusion_matrix(y_val, y_val_pred)
tn, fp, fn, tp = cm.ravel()

# Specificity
specificity = tn / (tn + fp)

# FDR (False Discovery Rate)
fdr = fp / (fp + tp) if (fp + tp) != 0 else 0

# FPR and TPR
fpr = fp / (fp + tn)
tpr = tp / (tp + fn)

# ROC and AUC
fpr_vals, tpr_vals, _ = roc_curve(y_val, y_val_proba)
roc_auc = auc(fpr_vals, tpr_vals)

# Display Confusion Matrix as Heatmap
plt.figure(figsize=(6, 4))
sns.heatmap(cm, annot=True, fmt='d', cmap='Blues')
plt.title('Confusion Matrix')
plt.xlabel('Predicted Label')
plt.ylabel('True Label')
plt.show()

# ROC Curve
plt.figure(figsize=(6, 4))
plt.plot(fpr_vals, tpr_vals, color='darkorange', lw=2, label='ROC curve (AUC = {:.2f})'.format(roc_auc))
plt.plot([0, 1], [0, 1], color='gray', linestyle='--')
plt.xlabel('False Positive Rate')
plt.ylabel('True Positive Rate')
plt.title('Receiver Operating Characteristic')
plt.legend(loc="lower right")
plt.show()

# Print metrics
print(f"Training Accuracy: {train_accuracy:.4f}")
print(f"Validation Accuracy: {val_accuracy:.4f}")
print(f"Best Threshold for F1: {best_thresh:.2f}")
print(f"Precision: {precision:.4f}")
print(f"Recall (TPR): {recall:.4f}")
print(f"F1 Score: {f1:.4f}")
print(f"Cohen Kappa Score: {kappa:.4f}")
print(f"Specificity (TNR): {specificity:.4f}")
print(f"False Discovery Rate (FDR): {fdr:.4f}")
print(f"False Positive Rate (FPR): {fpr:.4f}")
print(f"True Positive Rate (TPR): {tpr:.4f}")
print(f"ROC AUC Score: {roc_auc:.4f}")