import pandas as pd
from scipy.stats import ttest_rel
import numpy as np

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
    # Extract and force numeric conversion (errors='coerce' converts invalid values to NaN)
    normal_values = pd.to_numeric(df.iloc[i][normal_cols], errors='coerce').values
    tumor_values = pd.to_numeric(df.iloc[i][tumor_cols], errors='coerce').values

    # Remove pairs where either value is NaN
    mask = ~np.isnan(normal_values) & ~np.isnan(tumor_values)
    normal_clean = normal_values[mask]
    tumor_clean = tumor_values[mask]

    if len(normal_clean) > 1:
        t_stat, p_val = ttest_rel(normal_clean, tumor_clean)   
    else:
        p_val = np.nan  # Not enough data for test

    p_values.append(p_val)

# Build result DataFrame
result_df = pd.DataFrame({
    'Gene': genes,
    'Paired_P_Value': p_values
})

# Save to Excel
result_df.to_excel("paired_p_values.xlsx", index=False)

print("✅ Paired p-values saved to 'paired_p_values.xlsx'")


# import pandas as pd
# import numpy as np
# from statsmodels.stats.weightstats import ttest_ind

# # Load the dataset
# file_path = "merged_gene_of_normalized_values.xlsx"  # <-- update path if needed
# df = pd.read_excel(file_path)

# # Gene names
# genes = df.iloc[:, 0]

# # Find normal and tumor columns
# normal_cols = [col for col in df.columns if col.endswith('-N')]
# tumor_cols = [col for col in df.columns if col.endswith('-T')]

# normal_cols.sort()
# tumor_cols.sort()

# # Store p-values
# p_values = []

# for i in range(len(df)):
#     normal_values = pd.to_numeric(df.iloc[i][normal_cols], errors='coerce').values
#     tumor_values = pd.to_numeric(df.iloc[i][tumor_cols], errors='coerce').values

#     normal_clean = normal_values[~np.isnan(normal_values)]
#     tumor_clean = tumor_values[~np.isnan(tumor_values)]

#     if len(normal_clean) > 1 and len(tumor_clean) > 1:
#         t_stat, p_val, dfree = ttest_ind(normal_clean, tumor_clean,
#                                          alternative='two-sided',
#                                          usevar='pooled',
#                                          weights=(None, None),
#                                          value=0)
#         if np.isnan(p_val):
#             print(f"⚠️ NaN p-value for gene {genes.iloc[i]}")
#     else:
#         p_val = np.nan

#     p_values.append(p_val)


# # Create results DataFrame
# result_df = pd.DataFrame({
#     'Gene': genes,
#     'Unpaired_P_Value': p_values
# })

# # Save to Excel
# result_df.to_excel("unpaired_p_values.xlsx", index=False)

# print("✅ Unpaired p-values saved to 'unpaired_p_values.xlsx'")
