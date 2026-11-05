import pandas as pd
data={
    "name": ["Alice","Bob","Charlie","David","Emma","Frank"],
    "marks": [25,30,35,40,45,50],
    "age": [21,23,34,28,31,36] }
df=pd.DataFrame(data)
print(df.info())
print(df.describe())