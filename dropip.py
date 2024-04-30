import pandas as pd

def delete_rows_except_first(csv_file):
    # Read the CSV file into a DataFrame
    df = pd.read_csv(csv_file)

    # Keep only the first row and overwrite the CSV file
    df.head(1).to_csv(csv_file, index=False)

# Provide the path to your CSV file
csv_file_path = 'modified_dataset.csv'

# Call the function to delete all rows except the first row
delete_rows_except_first(csv_file_path)

print(f"All rows except the first row have been deleted in {csv_file_path}.")
