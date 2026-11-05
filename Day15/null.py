import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
df = pd.DataFrame({ 'Name': ['John', 'Alice', 'Bob'],
                    'Age': [25, None, 22], 
                    'Marks': [85, 90, None] })
print(df)
# print(df.isna())  # Checking for missing values
# print(df.isna().sum())  # Counting missing values in each column
# print(df.notna())
# print(df.notna().sum())  # Counting non-missing values in each column
#print(df[df['Age'].notna()])  # Filtering rows where Age and Marks are not missing
#sns.heatmap(df.isna())  # Visualizing missing values using a heatmap
#plt.show()
# print(df.dropna())  # Dropping rows with any missing values
# print(df.dropna(axis=1))  # Dropping columns with any missing values
# print(df.dropna(axis=0))  # Dropping rows with any missing values
# print(df.dropna(thresh=1))  # Dropping rows with less than 2 non-missing values

print(df.dropna(axis=1,thresh=2))  # Dropping columns with less than 2 non-missing values