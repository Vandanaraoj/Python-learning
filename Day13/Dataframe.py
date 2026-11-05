import pandas as pd
data={
    "name": ["Alice","Bob","Charlie"],
    "marks": [25, 30, 35],
    "age": [21,23,34]
}
df=pd.DataFrame(data)
print(df)
# print(df.index)
# print(df.columns)
# print(df.values)
print(df.marks)