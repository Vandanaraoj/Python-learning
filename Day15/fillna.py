import pandas as pd
df = pd.DataFrame({ 'Name': ['John', 'Alice', 'Arun', 'Bob'], 
                    'Marks': [85, 90, None, 45] })
print(df)
mean_value = df['Marks'].mean()  # Calculating the mean of the 'Marks' column
print(mean_value)
df['Marks']=df['Marks'].fillna(mean_value)  # Filling missing values with the mean
print(df)