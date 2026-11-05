import matplotlib.pyplot as plt
import seaborn as sns
marks = [45,50,55,60,60,65,70,70,75,90]
sns.histplot(marks,bins=20)
plt.xlabel('Marks')
plt.ylabel('Frequency')
plt.title('Distribution of Student Marks')
plt.show()