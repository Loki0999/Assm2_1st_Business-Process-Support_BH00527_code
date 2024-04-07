import pandas as pd

# Specify the path to the Excel file
excel_path = "data.xlsx"

# Read the Excel file into a DataFrame
df = pd.read_excel(excel_path)


# Function to handle special characters
def clean_special_characters(text):
    # Remove special characters using regular expressions
    cleaned_text = ''.join(e for e in text if e.isalnum() or e.isspace())
    return cleaned_text

# Apply the clean_special_characters function to each cell in the DataFrame
for column in df.columns:
    df[column] = df[column].astype(str).apply(clean_special_characters)

# Remove duplicate rows
df.drop_duplicates(inplace=True)

# Display the cleaned DataFrame
print(df)


# Specify the path for the cleaned Excel file
cleaned_excel_path = "cleaned_data.xlsx"

# Export the cleaned DataFrame to a new Excel file
df.to_excel(cleaned_excel_path, index=False)

print("Cleaned data has been exported to", cleaned_excel_path)