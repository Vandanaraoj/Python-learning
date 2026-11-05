import pandas as pd
df1 = pd.DataFrame({"name":["rahul","priya"],'marks': [85, 90]})
df2 = pd.DataFrame({"name":["arun","sneha"],'marks': [78, 88]})
result = pd.concat([df1, df2],ignore_index=True)
print(result)

df3 = pd.DataFrame({"name":["rahul","priya"]})
df4 = pd.DataFrame({'marks': [78, 88]})
result1 = pd.concat([df3, df4],axis=1)
print(result1)

df5 = pd.DataFrame({"name":["rahul","priya"],'marks': [78, 88]})
df6 = pd.DataFrame({"name":["arun","sneha"],'science': [32,34]})
result2 = pd.concat([df5, df6],axis=0,ignore_index=True)
print(result2)