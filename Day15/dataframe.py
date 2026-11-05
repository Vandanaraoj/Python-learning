import pandas as pd
df = pd.DataFrame({ 'Name': ['Alice', 'Bob', 'Charlie'], 
                    'Age': [25, 30, 35], 
                    'City': ['New York', 'Los Angeles', 'Chicago'] })
#print(df)
# print(df['Name'])
# # print(df['Age'])
# # print(df['City'])
# # print(df[['Name', 'Age', 'City']])
# print(df.loc[0])  # Accessing the first row
# print(df.loc[0, 'Age'])
# print(df.loc[0:1, ['Name','City']])  # Accessing rows 0 and 1 for the 'Name' column,'

# df.index = ['a', 'b', 'c']  # Setting custom index
# print(df)
# print(df.loc['a','City'])  # Accessing the row with index 'a'

# print(df.iloc[0])  # Accessing the first row using integer-location based indexing
# print(df.iloc[2, 2])  # Accessing the value in the first row and second column
# print(df.iloc[:,2])

# print(df.iloc[0:2, 0:2])  # Accessing rows 0 and 1 and columns 0 and 1

# print(df[df['Age'] >=25])  # Filtering rows where Age is greater than 30

# print(df.query('Age >= 25'))  # Using query method to filter rows where Age is greater than or equal to 30
print(df.query('Age > 56'))  # Using query method to filter rows where Age is greater than 56