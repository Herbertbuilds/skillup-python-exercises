#Panda Tutorial

import pandas as pd
import numpy as np

#Series
#Create a Series from a list
arr = [1,2,3,4,5]
s1 = pd.Series(arr)
#print(s1)

order = ['a','b','c','d','e']
s2 = pd.Series(arr, index=order)
#print(s2)

#modify our index
s1.index = ["a","b","c","d","e"]
#print(s1)

#Series operations
s3 = s1 + s2
#print(s3)

#Create a DataFrame
dates = pd.date_range('today', periods=6)
arr =np.random.Generator(6,4)
df1 = pd.DataFrame(arr, index=dates, columns=['A','B','C','D'])
#print(df1)

#Create a DataFrame from a dictionary
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David','Carl'],
    'Age': [24, 27, 22, 32,np.nan],
    'City': ['New York', 'Los Angeles', 'Chicago', 'Houston','New York']
}
labels = ['a','b','c','d','e']
df2 = pd.DataFrame(data, index=labels)
#print(df2)

string = pd.Series(['apple', 'banana', 'cherry', 'date',np.nan])
string.str.upper()
#print(string)

#DataFrame operations
#df2.fillna()#fill missing values
df3 = df2.copy()
df3 = df2.dropna()#drop rows with missing values
#print(df3)

#data frames file operations
df2.to_csv('data.csv')#save to csv
df2_data = pd.read_csv('data.csv')#read from csv
print(df2_data)


df2.to_excel('data.xlsx', sheet_name='Sheet1')#save to excel    