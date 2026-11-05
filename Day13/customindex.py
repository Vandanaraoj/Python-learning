import pandas as pd
marks=pd.Series([80,90,75], index=['Alice', 'Bob', 'Charlie'])
print(marks)
print(marks['Bob'])  # Accessing a specific value by index