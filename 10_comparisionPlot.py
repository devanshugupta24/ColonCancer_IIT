# #BAR PLOT


# import pandas as pd                # Import pandas for reading Excel files
# import matplotlib.pyplot as plt    # Import matplotlib for plotting
# # Load the filtered Excel file containing selected genes
# df = pd.read_excel("filtered_genes.xlsx")
# # Extract gene names and their average expression values in Normal and Tumor samples
# genes = df["Gene"]                 # Gene names
# normal = df["Average-N"]          # Average expression in normal tissue
# tumor = df["Average-T"]           # Average expression in tumor tissue
# # Generate x-axis positions for the bars
# x = range(len(genes))
# plt.figure(figsize=(14, 6))       # Set figure size
# # Plot normal values as bars
# plt.bar(x, normal, width=0.4, label="Normal", align='center')
# plt.bar([i + 0.4 for i in x], tumor, width=0.4, label="Tumor", align='center')  # Plot tumor values near to the right
# # Set x-axis tick labels in the center between normal and tumor bars
# plt.xticks([i + 0.2 for i in x], genes, rotation=90)
# # Add labels and title
# plt.ylabel("Average Expression")              # Y-axis label
# plt.title("Gene Expression: Normal vs Tumor") # Plot title
# plt.legend()                                  # Show legend
# plt.tight_layout()
# plt.show()


###############################################################
##BAR PLOT with LOG values
# import pandas as pd
# import matplotlib.pyplot as plt

# # Load the data
# df = pd.read_excel("filtered_genes.xlsx")

# # Extract values
# genes = df["Gene"]
# normal = df["Average_N"]
# tumor = df["Average_T"]
# x = range(len(genes))

# # Plot with log scale
# plt.figure(figsize=(14, 6))
# plt.bar(x, normal, width=0.4, label="Normal", align='center')
# plt.bar([i + 0.4 for i in x], tumor, width=0.4, label="Tumor", align='center')

# plt.xticks([i + 0.2 for i in x], genes, rotation=90)
# plt.ylabel("Average Expression (log scale)")
# plt.yscale("log")  # Apply logarithmic scale to y-axis
# plt.title("Gene Expression: Normal vs Tumor (Log Scale)")
# plt.legend()
# plt.tight_layout()
# plt.show()


# ## SCATTER WITH BOX AND WHISKER
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the Excel file (make sure the path is correct)
df = pd.read_excel("filtered_genes.xlsx")

def plot_gene_expression(gene_name):
    gene_row = df[df['Gene'] == gene_name]
    if gene_row.empty:
        print(f"❌ Gene '{gene_name}' not found in the dataset.")
        return

    normal_cols = [col for col in df.columns if '-N' in col]
    tumor_cols = [col for col in df.columns if '-T' in col]

    normal_vals = gene_row[normal_cols].values.flatten() + 0.1
    tumor_vals = gene_row[tumor_cols].values.flatten() + 0.1

    plot_df = pd.DataFrame({
        'Expression': np.concatenate([normal_vals, tumor_vals]),
        'Condition': ['Normal'] * len(normal_vals) + ['Tumor'] * len(tumor_vals)
    })

    plt.figure(figsize=(8, 4))
    sns.boxplot(x='Condition', y='Expression', data=plot_df, whis=1.5, showfliers=False,
                palette=['#1f77b4', '#ff7f0e'])
    sns.stripplot(x='Condition', y='Expression', data=plot_df, color='black', jitter=False, size=5, alpha=0.7)

    plt.title(f"Gene Expression of {gene_name} (Normal vs Tumor) [Normal Scale]")
    plt.xlabel("Condition")
    plt.ylabel("Gene Expression Value")
    plt.grid(axis='y', linestyle='--', alpha=0.2)

    # Optional: add median values on the plot
    medians = plot_df.groupby('Condition')['Expression'].median()
    for i, median in enumerate(medians):
        plt.text(i, median, f"{median:.2f}", ha='center', va='bottom', fontsize=9, color='black', weight='semibold')

    plt.tight_layout()
    plt.show()


# Example usage:
plot_gene_expression("AJUBA")
