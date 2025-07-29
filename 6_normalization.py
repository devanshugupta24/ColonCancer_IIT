import pandas as pd

# Step 1: Load your dataset
file_path = 'merged_genes_with_avg.xlsx'  
df = pd.read_excel(file_path, index_col=0)

# Step 2: Separate Normal and Tumor columns (assuming alternating order)
normal_cols = df.columns[::2]   # every 1st, 3rd, 5th... column
tumor_cols = df.columns[1::2]   # every 2nd, 4th, 6th... column

# Step 3: Compute mean and std separately for Normal and Tumor
normal_mean = df[normal_cols].mean(axis=1)
normal_std = df[normal_cols].std(axis=1) + 1e-8  # avoid div by zero
tumor_mean = df[tumor_cols].mean(axis=1)
tumor_std = df[tumor_cols].std(axis=1) + 1e-8

# Step 4: Normalize values   Z-SCORE NORMALIZATION
df_normal_z = df[normal_cols].subtract(normal_mean, axis=0).divide(normal_std, axis=0)   
df_tumor_z = df[tumor_cols].subtract(tumor_mean, axis=0).divide(tumor_std, axis=0)

# Step 5: Recombine columns in original alternating order
normalized_df = pd.DataFrame(index=df.index)
for n_col, t_col in zip(df_normal_z.columns, df_tumor_z.columns):
    normalized_df[n_col] = df_normal_z[n_col]
    normalized_df[t_col] = df_tumor_z[t_col]

# Step 6: Export to Excel
normalized_df.to_excel('zscore_normalized_separately.xlsx')

