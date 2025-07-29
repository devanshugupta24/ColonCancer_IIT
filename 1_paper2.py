import pandas as pd

# Load your Excel file
df = pd.read_excel('datos_editable (1).xlsx')

# Transpose the dataframe (columns become rows, rows become columns)
df_transposed = df.transpose()

# Optionally, reset index to make the original column names a column
df_transposed = df_transposed.reset_index()
df_transposed.columns = ['New_Row_Names'] + list(df_transposed.columns[1:])

# Save the result to a new Excel file if needed
df_transposed.to_excel('paper1final.xlsx', index=False)
