import pandas as pd
df1 = pd.DataFrame({'student_id': [101, 102,103],"name":["rahul","priya","arun"]})
df2=pd.DataFrame({"id": [101, 102,103],"math":[45,56,67]})
result= pd.merge(df1, df2, left_on='student_id', right_on='id')
print(result)