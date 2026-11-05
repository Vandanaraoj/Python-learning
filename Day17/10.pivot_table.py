import pandas as pd
df=pd.DataFrame({"student":["arun","priya","rahul","anil","sita","lohith"],
                "gender":["m","f","m","f","f","m"],
                "city":["bang","bang","chennai","chennai","bang","chennai"],
                "marks":[80,90,40,70,30,20]})
# print(df)
print(df.pivot_table(values="marks",index="city",columns="gender",aggfunc="mean"))
