import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
df=pd.DataFrame({ 'Hours':[1,2,3,4,5],"marks":[40,50,60,70,80],"sleep":[8,7,6,5,4]})
corr = df.corr()
sns.heatmap(corr, annot=True)
plt.show()