import pandas as pd
df=pd.DataFrame({"name":["A","B","C","D","E","F"],
              "city":["Bangalore","Bangalore","Chennai","Chennai","Bangalore","Chennai"],
              "subject":["Maths","Science","Maths","Science","Maths","Maths"],
              "marks":[80,90,70,85,95,75]})
print(df)
# print(df.groupby("city")["marks"].mean())
# print(df.groupby("city")["marks"].sum())
# print(df.groupby("city")["name"].count())
# print(df.groupby("city")["marks"].agg(["mean", "min", "max","sum","count"]))

#print(df.groupby(["city","subject"])["marks"].mean())
print(df.groupby(["city","subject"])["marks"].agg(["mean", "min", "max","sum","count"]))