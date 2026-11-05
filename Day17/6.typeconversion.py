import pandas as pd
df = pd.DataFrame({"Age":["25","30","49","40"]})
print(df.dtypes)

df["Age"]=pd.to_numeric(df["Age"])  
print(df)
print(df.dtypes)