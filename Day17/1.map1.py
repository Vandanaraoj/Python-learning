import pandas as pd
df = pd.DataFrame({"name":["ravi","priya","rahul","jyothika"],
                  "gender_code":[1,2,1,2]})

#print(df)
gender_map={1:"male",2:"female"}
# df["gender"]=df["gender_code"].map(gender_map)
# print(gender_map[1])
# print(gender_map[3]) # KeyError: 3

df["gender"]=df["gender_code"].replace(gender_map)
print(df)
print(gender_map[1])
print(gender_map[3])