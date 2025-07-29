import pandas as pd

# Load the Excel file
file_path = "merged_genes_with_avg_and_pvalue.xlsx"
df = pd.read_excel(file_path)

# Check the column name for adjusted p-value (adjust if needed)
# Example: it might be named 'adj.P.Val' or 'adjusted_p_value'
# Let's assume it’s called 'adj.P.Val'
filtered_df = df[(df['Adjusted_P_Value_FDR_BH'] < 0.1) & (df['Adjusted_P_Value_FDR_BH'].notnull())]

# Save filtered genes to a new Excel or CSV file (optional)
filtered_df.to_excel("filtered_genes_adj_pval_below_0.1.xlsx", index=False)

# Show how many genes passed the filter
print(f"Number of genes with adjusted p-value < 0.1: {filtered_df.shape[0]}")
