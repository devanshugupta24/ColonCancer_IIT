import pandas as pd

# Load the original merged file (with 'N/A' as string)
df = pd.read_excel('merged_genes_filled_with_0.xlsx', header=[0, 1], index_col=0)

# Identify columns with Normal and Tumor
normal_cols = [col for col in df.columns if col[1].lower() == 'normal']
tumor_cols = [col for col in df.columns if col[1].lower() == 'tumor']

# Calculate averages (treating N/A as 0)
avg_normal = df[normal_cols].mean(axis=1)
avg_tumor = df[tumor_cols].mean(axis=1)

# Build average columns
average_df = pd.concat([avg_normal, avg_tumor], axis=1)
average_df.columns = pd.MultiIndex.from_tuples([('Average', 'Normal'), ('Average', 'Tumor')])

# Append average columns to original data (which still contains 'N/A')
df_with_avg = pd.concat([df, average_df], axis=1)

# Save to Excel
df_with_avg.to_excel('merged_genes_with_avg.xlsx')
