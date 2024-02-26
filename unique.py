import pandas as pd
 
# Replace 'your_file.xlsx' with your actual excel file path
file_path = r"<filepath>"

# Read the excel file into a dataframe. I'm skipping the top 2 rows due to the unique header/subheader
# layout
df = pd.read_excel(file_path, skiprows=2)

# Display column headers
column_headers = df.columns
print("Column Headers:")
print(column_headers)

# Get unique values and their counts for column 'X'
unique_values = df['X'].unique() 

print("Unique Values in Column 'X':")
print(unique_values)
# From 1/8 file: [...
# ]
# this is _ agency codes

# From 2/12 file: [...  
# ]
# this is _ agency codes

# Count the number of unique values for column 'X'
num_unique_values = df['X'].nunique()

print("\nNumber of Unique Values in Column 'X':")
print(num_unique_values)
# __

# --------------

# Replace 'your_file.xlsx' with your actual Excel file path
file_path_2 = r"<filepath>"

# Read the Excel file into a DataFrame
df_2 = pd.read_excel(file_path_2)

# Display column headers
column_headers_2 = df_2.columns
print("Column Headers:")
print(column_headers_2)

# Get unique values and their counts for column 'Y'
unique_values_2 = df_2['Y'].unique()
print("Unique Values in Column 'Y':")
print(unique_values_2)

# Count the number of unique values for column 'Y'
num_unique_values_2 = df_2['Y'].nunique()
# From 1_8 file: [
# ]
# this is __ agency codes

# From 2/12 file: [ 
# ]
# this is __ agency codes

print("\nNumber of Unique Values in Column 'Y':")
print(num_unique_values_2)
# __
# __

# ------

# Compare the two lists and show me which overlap

grantinfo = [numbers a-z]
rpfrmelt = [numbers a-z]

common_numbers = set(grantinfotab).intersection(set(rpfrmelt))

print("Common numbers:", common_numbers)
# Common numbers: { ... }

numbers_not_in_rpfrmelt = set(grantinfo) - set(rpfrmelt)

print("Numbers in grantinfo that are not in rpfrmelt:", numbers_not_in_rpfrmelt)

# Numbers in grantinfo that are not in rpfrmelt: {...}
