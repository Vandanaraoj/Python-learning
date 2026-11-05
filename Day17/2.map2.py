import pandas as pd
df = pd.DataFrame({"marks":[10,20,30,40]})
print(df)
df["double"]=df["marks"].map(lambda x:x*2)
print(df)