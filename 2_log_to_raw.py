import pandas as pd
import numpy as np

# Load the Excel file
df = pd.read_excel("paper1final.xlsx", index_col=0)

# Convert all values to numeric, force errors to NaN
df_numeric = df.apply(pd.to_numeric, errors='coerce')

# Apply the 2^x transformation
converted_df = np.power(2, df_numeric)

# Save the converted data to a new Excel file
converted_df.to_excel("paper1final_converted.xlsx")
