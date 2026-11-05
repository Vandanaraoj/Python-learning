def get_grade(marks):
    if marks>=90:
        return "A"
    elif marks>=75:
        return "B"
    elif marks>=50:
        return "C"
    else:
        return "F"

import pandas as pd
df = pd.DataFrame({"name":["ravi","priya","rahul","jyothika"], "marks":[90,78,100,40]}) 
print(df)
df["grade"]=df["marks"].apply(get_grade) 
print(df)

df["double"]=df["marks"].map(lambda x:x*2)
print(df)