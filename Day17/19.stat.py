import pandas as pd
df=pd.DataFrame({ 'Hours':[1,2,3,4,5],"marks":[40,50,60,70,80],"sleep":[8,7,6,5,4]})
#print(df.corr()) # Pearson correlation  >> print(df.corr(method='pearson'))
#print(df.corr(method='spearman'))
print(df.corr(method='pearson'))