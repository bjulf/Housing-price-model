import pandas as pd


# Load the CSV file into a DataFrame
df = pd.read_csv(r'C:\Users\Bjorn\OneDrive - ZEM AS\Studier\Multivariate Data-Analysis\DA-3\raw_data_2024_10\market_transactions.csv')


# Filter the DataFrame to include only rows where 'official_date' is after 2019
df['official_date'] = pd.to_datetime(df['official_date'], errors='coerce')

# Remove rows with invalid data in 'official_date', 'address_id', or 'official_price'
df = df.dropna(subset=['official_date', 'address_id', 'official_price'])

#Remove any housing sold after 2019
df = df[df['official_date'] > '2019-12-31']


# Keep only the specified columns
df = df[['official_date', 'address_id', 'official_price']]

# Rename 'official_date' to 'sold_date'
df = df.rename(columns={'official_date': 'sold_date'})


# Check for NaN values in the dataset
if df.isnull().values.any():
    print("There are NaN values in the dataset.")
    print(df.isnull().sum())
else:
    print("No NaN values found in the dataset.")


#save the modified DataFrame back to a CSV file
df.to_csv(r'C:\Users\Bjorn\OneDrive - ZEM AS\Studier\Multivariate Data-Analysis\DA-3\Processed data\market_transactions_cleaned.csv', index=False)
