import pandas as pd
df = pd.DataFrame({"math":[85,75,95,35],
                    "science":[90,78,100,40],
                    "English":[30,45,65,38]})
result = df.apply(lambda column: column.mean())
#result = df.apply(lambda df["math"]: df["math"].mean()) # Invalid syntax : it will not fetch single column mean
print(result)