import pandas as pd

# Load the Excel file
file_path = 'cardio_train(LVQ, KNN, KMEANS) (1).xlsx'
xls = pd.ExcelFile(file_path)

# Display sheet names to understand the structure
sheet_names = xls.sheet_names
sheet_names
