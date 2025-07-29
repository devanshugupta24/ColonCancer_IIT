import pandas as pd
from scipy.stats import ttest_rel
import numpy as np
from statsmodels.stats.multitest import multipletests

# Load your file
file_path = "merged_genes_with_avg.xlsx"  # Update if needed
df = pd.read_excel(file_path)

# Get gene names
genes = df.iloc[:, 0]

# Find normal and tumor columns
normal_cols = [col for col in df.columns if col.endswith('-N')]
tumor_cols = [col for col in df.columns if col.endswith('-T')]

normal_cols.sort()
tumor_cols.sort()

# Container for p-values
p_values = []

for i in range(len(df)):
    normal_values = pd.to_numeric(df.iloc[i][normal_cols], errors='coerce').values
    tumor_values = pd.to_numeric(df.iloc[i][tumor_cols], errors='coerce').values

    mask = ~np.isnan(normal_values) & ~np.isnan(tumor_values)
    normal_clean = normal_values[mask]
    tumor_clean = tumor_values[mask]

    if len(normal_clean) > 1:
        t_stat, p_val = ttest_rel(normal_clean, tumor_clean)
    else:
        p_val = np.nan

    p_values.append(p_val)

# Adjust p-values with FDR Benjamini-Hochberg
# Filter out NaN before adjustment
valid_pvals = [p for p in p_values if not np.isnan(p)]
adjusted = multipletests(valid_pvals, alpha=0.1, method='fdr_bh')

# Fill adjusted p-values, keeping NaN for skipped rows
adjusted_p_values = []
valid_idx = 0
for p in p_values:
    if np.isnan(p):
        adjusted_p_values.append(np.nan)
    else:
        adjusted_p_values.append(adjusted[1][valid_idx])
        valid_idx += 1

# Build final DataFrame
result_df = pd.DataFrame({
    'Gene': genes,
    'Paired_P_Value': p_values,
    'Adjusted_P_Value_FDR_BH': adjusted_p_values
})

# Save to Excel
result_df.to_excel("paired_p_values_adjusted.xlsx", index=False)

print("✅ Paired & FDR-adjusted p-values saved to 'paired_p_values_adjusted.xlsx'")


# import pandas as pd
# import numpy as np
# from statsmodels.stats.weightstats import ttest_ind
# from statsmodels.stats.multitest import multipletests

# # Load the Excel file
# file_path = "merged_gene_of_normalized_values.xlsx"  # Replace with your path if needed
# df = pd.read_excel(file_path)

# # Extract gene names
# genes = df.iloc[:, 0]

# # Identify normal and tumor columns
# normal_cols = [col for col in df.columns if col.endswith('-N')]
# tumor_cols = [col for col in df.columns if col.endswith('-T')]

# normal_cols.sort()
# tumor_cols.sort()

# # Store raw p-values
# p_values = []

# # Run unpaired t-test for each gene
# for i in range(len(df)):
#     normal_values = pd.to_numeric(df.iloc[i][normal_cols], errors='coerce').values
#     tumor_values = pd.to_numeric(df.iloc[i][tumor_cols], errors='coerce').values

#     # Drop NaN values
#     normal_clean = normal_values[~np.isnan(normal_values)]
#     tumor_clean = tumor_values[~np.isnan(tumor_values)]

#     if len(normal_clean) > 1 and len(tumor_clean) > 1:
#         t_stat, p_val, dfree = ttest_ind(
#             normal_clean, tumor_clean,
#             alternative='two-sided',
#             usevar='pooled',
#             weights=(None, None),
#             value=0
#         )
#     else:
#         p_val = np.nan

#     p_values.append(p_val)

# # Filter valid p-values (non-NaN) for adjustment
# valid_pvals = [p for p in p_values if not np.isnan(p)]

# # Apply Holm–Šidák correction with alpha = 0.1
# adjusted = multipletests(
#     valid_pvals,
#     alpha=0.1,
#     method='hs',
#     maxiter=1,
#     is_sorted=False,
#     returnsorted=False
# )

# # Fill adjusted p-values back, preserving original gene order
# adjusted_p_values = []
# valid_idx = 0
# for p in p_values:
#     if np.isnan(p):
#         adjusted_p_values.append(np.nan)
#     else:
#         adjusted_p_values.append(adjusted[1][valid_idx])
#         valid_idx += 1

# # Build results DataFrame
# result_df = pd.DataFrame({
#     'Gene': genes,
#     'Raw_Unpaired_P_Value': p_values,
#     'Adjusted_P_Value_Holm_Sidak': adjusted_p_values
# })

# # Save to Excel
# result_df.to_excel("unpaired_p_values_Holm_Sidak.xlsx", index=False)

# print("✅ Unpaired t-test with Holm–Šidák adjustment done. File saved as 'unpaired_p_values_Holm_Sidak.xlsx'.")
