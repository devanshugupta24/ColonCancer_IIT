import pandas as pd

# Load the Excel file
df = pd.read_excel("merged_genes.xlsx", index_col=0)

# Fill all blank or missing values with 0
df_filled = df.fillna(0)

# Save the cleaned DataFrame to a new Excel file
df_filled.to_excel("merged_genes_filled_with_0.xlsx")
