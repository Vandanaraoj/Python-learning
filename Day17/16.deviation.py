import pandas as pd
df1 = pd.DataFrame({'marks': [2, 7,3,12,9]})
range = (df1['marks'].max() - df1['marks'].min())
mean = df1['marks'].mean()  #(2+7+3+12+9)/5 = 33/5 = 6.6
variance = df1['marks'].var() #((6.6-2)^2 + (6.6-7)^2 + (6.6-3)^2 + (12-6.6)^2 + (9-6.6)^2)/5
std = df1['marks'].std() #sqrt(variance)
print(f"Range: {range}")
print(f"Mean: {mean}")
print(f"Variance: {variance}")
print(f"Standard Deviation: {std}")