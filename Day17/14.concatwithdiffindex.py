import pandas as pd
df5 = pd.DataFrame({"name":["rahul","priya"]}, index=[1,2])
df6 = pd.DataFrame({'marks': [32,34]}, index=[1,2])
result2 = pd.concat([df5, df6],axis=1)
print(result2)

df7 = pd.DataFrame({"name":["rahul","priya"]}, index=[1,2])
df8 = pd.DataFrame({'marks': [32,34]}, index=[3,5])
result3 = pd.concat([df7, df8],axis=1)
print(result3)