import pandas as pd
df = pd.DataFrame({"Age":["25","30","49","40","unknown"]})
print(df.dtypes)

#df["Age"]=pd.to_numeric(df["Age"]) # Value error :ValueError: invalid literal for int() with base 10: 'unknown 
df["Age"]=pd.to_numeric(df["Age"],errors="coerce") # Handle conversion errors
print(df)
print(df.dtypes)