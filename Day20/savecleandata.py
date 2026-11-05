import pandas as pd
from datetime import datetime
data=[{"name": "John", "age": 30, "marks": 85}, {"name": "Rahul", "age": 25, "marks": 90}, {"name": "Aru", "age": 35, "marks": 78}]
df = pd.DataFrame(data)
#Clean the data
df["age"] = df["age"].fillna(df["age"].mean())
df["marks"] = df["marks"].fillna(df["marks"].mean())
# Generate time stamp
timestamp=datetime.now().strftime("%Y%m%d %H%M%S")
# create filename
filename = f"clean_data_{timestamp}.csv"
#Save the cleandata
df.to_csv(filename, index=False)
print("Cleaned data saved to", filename)