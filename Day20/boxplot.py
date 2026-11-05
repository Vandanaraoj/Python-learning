import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
df=pd.DataFrame({'course':["python"]*3+["SQL"]*3+["Excel"]*3,'marks':[80,90,70,65,75,85,55,65,75]})
sns.boxplot(data=df,x='course',y='marks')
plt.title('Marks distribution by Course')
plt.xlabel('Course')
plt.ylabel('Marks')
plt.show()