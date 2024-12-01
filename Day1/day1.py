import csv
import pandas as pd

data = pd.read_csv('Day1/data.csv', header=None, sep='  ')
data.columns = ['1', '2']


#Part 1
data ['1']= data['1'].sort_values().reset_index(drop=True)
data ['2']= data['2'].sort_values().reset_index(drop=True)
data['diff']=(data['2'].sort_values()-data['1'].sort_values()).abs()

print(data.sum())

#Part 2
data['1_occurence_in_2'] = data['1'].apply(lambda x: (data['2'] == x).sum())
data['similarity'] = data['1']*data['1_occurence_in_2']

print(data.sum())