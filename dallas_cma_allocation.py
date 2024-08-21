import pandas as pd

# Sample list of ZIP codes in Dallas (In practice, you would load this from a reliable source)
dallas_zip_codes = [
    "75201", "75202", "75203", "75204", "75205", "75206", "75207", "75208", "75209", "75210",
    "75211", "75212", "75214", "75215", "75216", "75217", "75218", "75219", "75220", "75221"
]

# Convert the list of ZIP codes into a pandas DataFrame
df_zip = pd.DataFrame(dallas_zip_codes, columns=["ZIP5_CD"])

# Allocate CMA numbers by grouping ZIP codes in batches of 3-4
df_zip['CMA_CD'] = (df_zip.index // 3) + 1  # CMA_CD will increment for every 3 ZIP codes

# Display the resulting DataFrame
print(df_zip)

# Optionally, save the result to a CSV file
output_path = "dallas_zip_to_cma.csv"  # Replace with your desired file path
df_zip.to_csv(output_path, index=False)
