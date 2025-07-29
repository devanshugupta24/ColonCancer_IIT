import pandas as pd

# Load both Excel files
file1 = pd.read_excel('paper2final.xlsx', header=[0, 1], index_col=0)
file2 = pd.read_excel('paper1final_converted.xlsx', header=[0, 1], index_col=0)

# Merge them on the gene names (index)
merged = pd.concat([file1, file2], axis=1)

# Optional: Sort the index and columns
merged.sort_index(inplace=True)
merged = merged.reindex(sorted(merged.columns), axis=1)

# Save the merged result to a new Excel file
merged.to_excel('merged_genes.xlsx')
