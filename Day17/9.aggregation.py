import pandas as pd
df=pd.DataFrame({"math":[20,30,40],
                    "science":[20,30,40],
                    "English":[20,30,40]})
print(df)
result=df.agg({"math":"sum","science":"mean"})
print(result)