import pandas as pd
from pathlib import Path

# ------------------------------------------------------------------
# 1. CONFIG – change file names here if yours differ
# ------------------------------------------------------------------
EXCEL_FILE   = "filtered_genes_adj_pval_below_0.1.xlsx"
FEATURE_FILE = "gene_feature_order.txt"      # one gene per line

# ------------------------------------------------------------------
# 2. LOAD feature order
# ------------------------------------------------------------------
with open(FEATURE_FILE) as f:
    feature_order = [line.strip() for line in f if line.strip()]

print(f"Loaded feature order: {len(feature_order):,} genes")

# ------------------------------------------------------------------
# 3. LOAD expression matrix (row index = sample ID, columns = genes)
#     ➔ If your Excel file has separate sample-ID column, adjust below.
# ------------------------------------------------------------------
expr = pd.read_excel(EXCEL_FILE, index_col=0).T
print(f"Loaded expression sheet: {expr.shape[0]:,} samples × {expr.shape[1]:,} genes")

# ------------------------------------------------------------------
# 4. Ask for patient/sample ID
# ------------------------------------------------------------------
sample_id = input("Enter patient/sample ID-").strip()

if sample_id not in expr.index:
    print(f"Available samples: {', '.join(expr.columns)}")
    raise ValueError(f"Sample '{sample_id}' not found in the Excel sheet!")

# ------------------------------------------------------------------
# 5. Re-order genes to match the model
# ------------------------------------------------------------------
missing = [g for g in feature_order if g not in expr.columns]
if missing:
    raise ValueError(f"{len(missing)} genes in feature list are missing from the sheet, "
                     "e.g. " + ", ".join(missing[:10]))

vals = expr.loc[sample_id, feature_order]

# ------------------------------------------------------------------
# 6. Write to <sample>_gene_values.txt (one line, comma-separated)
# ------------------------------------------------------------------
out_path = Path(f"{sample_id}_gene_values.txt")
out_path.write_text(",".join(map(str, vals.astype(float).values)))

print(f"✅  Saved  {out_path.name}  ({len(feature_order):,} genes)")
