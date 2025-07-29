import joblib
import pandas as pd
import numpy as np

# Load model
model = joblib.load("xgb_model_thresh_0.4.pkl")


# 2. load the canonical feature list
with open("gene_feature_order.txt") as f:
    feat_order = [l.strip() for l in f]

# 3. Load comma-separated values from .txt as a list
with open("P2-T_gene_values.txt") as f:
    raw_line = f.read().strip()

gene_values = [float(x) for x in raw_line.split(",")]

# 4. Build a DataFrame with correct shape and column names
new_sample = pd.DataFrame([gene_values], columns=feat_order)


# Predict probabilities
proba = model.predict_proba(new_sample)[:, 1]

# Use your custom threshold
threshold = 0.4
pred = (proba >= threshold).astype(int)

# Output result
print("Prediction:", "Cancer" if pred[0] == 1 else "Healthy")
print("Probability of Cancer:", proba[0])
