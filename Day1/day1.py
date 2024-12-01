import pandas as pd

# Read the CSV file into a DataFrame
data = pd.read_csv('Day1/data.csv', header=None, sep='  ')
data.columns = ['1', '2']

# Part 1
# Sort the values in columns '1' and '2' and reset their indices
data['1'] = data['1'].sort_values().reset_index(drop=True)
data['2'] = data['2'].sort_values().reset_index(drop=True)

# Calculate the absolute difference between the sorted columns
data['diff'] = (data['2'].sort_values() - data['1'].sort_values()).abs()

# Print the sum of all columns
print(data.sum())

# Part 2
# Count the occurrences of each value in column '1' within column '2'
data['1_occurence_in_2'] = data['1'].apply(lambda x: (data['2'] == x).sum())

# Calculate the similarity as the product of column '1' and its occurrences in column '2'
data['similarity'] = data['1'] * data['1_occurence_in_2']

# Print the sum of all columns
print(data.sum())