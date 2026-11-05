import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
df=pd.DataFrame({'Department':['python','python','SQL','SQL','pandas','pandas'],'marks':[80,90,70,60,85,95]})
sns.barplot(data=df,x='Department',y='marks')
plt.title('Average Marks by department')
plt.xlabel('Department')
plt.ylabel('Marks')
plt.show()