# file = open('new_data.csv','x')
# file.close()

import pandas as pd
df = pd.read_csv('new_data.csv',index_col = 'sn')
print(df)
# print(df.head(1))
# print(df.tail(1))

# iloc vaneko index anusaar and loc vaneko chaenaame anusaar
print(df.iloc[2:5])
print(df.loc[2:5])
df = pd.read_csv('new_data.csv',index_col = 'name')
print(df.loc['Shyam':'Nabin'])

b = df[(df['add'] == 'Kathmandu') & (df['age']>40)]
print(b)

import csv
info =[['name','age','add'],
       ['Ram',45,'Kathmandu'],
       ['Shyam',25,'Bhaktapur'],
       ['Hari',67,'Lalitpur']]
file = open('list_data.csv','w')
x = csv.writer(file)
x.writerows(info)
file.close()

import pandas as pd
df = pd.read_csv('list_data.csv')
print(df)

import csv
with open('list_data.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        print(row)

import csv
data = [{'name': 'Ram', 'age': '45', 'add': 'Kathmandu'},
        {'name': 'Shyam', 'age': '25', 'add': 'Bhaktapur'},
        {'name': 'Hari', 'age': '67', 'add': 'Lalitpur'}]
c = ['name','age','add'] 
with open('data.csv','w') as csvfile:
    writer = csv.DictWriter(csvfile,fieldnames=c)
    writer.writeheader()
    writer.writerows(data)

df = pd.read_csv('data.csv')
print(df)

import pandas as pd
data = {'name':['Ram','Shyam','Hari'],
        'age':[34,56,78],
        'add':["Kathmandu","Bhaktapur","Lalitpur"]}
df = pd.DataFrame(data)
df.to_csv('dataframe.csv')
print(df)

df = pd.read_csv('dataframe.csv',usecols = ['name','age','add'])
print(df)

import pandas as pd
data1 = {'name':['Ram','Shyam','Hari'],
        'age':[34,56,78],
        'add':["Kathmandu","Bhaktapur","Lalitpur"]}
data2 = {'name':['Ram','Shyam','Hari'],
        'age':[34,56,78],
        'add':["Kathmandu","Bhaktapur","Lalitpur"]}
df1 = pd.DataFrame(data1)
df2 = pd.DataFrame(data2)
df = pd.concat([df1,df2])
print(df)