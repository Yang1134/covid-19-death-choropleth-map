import pandas as pd

# Read the CSV file into a Pandas DataFrame
df = pd.read_csv('owid-covid-data.csv')

# Group the DataFrame by the 'location' column and find the maximum total deaths in each group
max_deaths_by_location = df.groupby('location')['total_deaths'].max().reset_index()

# Rename the columns for clarity
max_deaths_by_location.columns = ['Country', 'Highest Total Deaths']

# Save the result as a new CSV file
max_deaths_by_location.to_csv('max_deaths_by_location.csv', index=False)

print("Result saved as 'max_deaths_by_location.csv'")
