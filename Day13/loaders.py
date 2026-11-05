import pandas as pd
df=pd.read_csv("sales.csv",parse_dates=["date"])
print(df)
print(df.dtypes)
print(df['date'].dt.year) # Accessing the year from the date column
print(df['date'].dt.month) # Accessing the month from the date column
print(df['date'].dt.day) # Accessing the day from the date column