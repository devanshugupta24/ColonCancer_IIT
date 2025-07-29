import pandas as pd

# Load the Excel file
df = pd.read_excel("merged_genes_with_avg.xlsx")  # Replace with your file path if needed

# List of target genes
target_genes = [
    "fgf19", "nr0b1", "nr0b2", "hes1", "hes7", "lgr5", "krt20", "lyz", "hnf4",
    "fas", "gpbar1", "hspa9", "hspa14", "hspg2", "fxr1", "fxr2", "scn7a", "epha7",
    "myc", "krt23", "TGFBI", "KIAA1199", "COL11A1", "COL10A1", "ctnnb1", "axin2",
    "ets2", "dpep1", "LPAR1", "AJUBA", "EGFL6", "cdk1", "ect2", "rnf43", "cdx2",
    "tp53", "heph", "mep1a", "hnf4a", "hspg2", "apcdd1", "ptch1", "prox1", "tgr5",
    "cyp7a1", "fabp6", "lyz"
]

# Convert genes to lowercase for case-insensitive matching
target_genes_lower = [gene.lower() for gene in target_genes]

# Filter the DataFrame
filtered_df = df[df['Gene'].astype(str).str.lower().isin(target_genes_lower)]

# Save to a new Excel file
filtered_df.to_excel("filtered_genes.xlsx", index=False)
