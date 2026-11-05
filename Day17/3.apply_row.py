from turtle import pd


def check_eligiblity(row):
 if row["marks"]>=50 and row["attendance"]>=75:
    return "Eligible"
 else:
    return "Not Eligible"

import pandas as pd
df= pd.DataFrame({"name":["ravi","priya","rahul","jyothika"],
                 "marks":[90,78,100,40], "attendance":[80,70,90,60]})
df["eligibility"]=df.apply(check_eligiblity,axis=1)
print(df)