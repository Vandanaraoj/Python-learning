import pandas as pd
df = pd.DataFrame({'salary': [9,10,12,14,15,16,18,19,20,22,24,26,60]})
QA1 = df['salary'].quantile(0.25)
print(f"QA1: {QA1}")
QA3 = df['salary'].quantile(0.75)
print(f"QA3: {QA3}")
IQR = QA3 - QA1
print(f"IQR: {IQR}")
lower = QA1 - 1.5 * IQR
upper = QA3 + 1.5 * IQR
outliers = df[(df['salary'] < lower) | (df['salary'] > upper)]
print(f"Lower Limit: {lower}")
print(f"Upper Limit: {upper}")
print(outliers)