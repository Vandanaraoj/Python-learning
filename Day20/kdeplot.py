import matplotlib.pyplot as plt
import seaborn as sns
marks = [45,50,55,60,60,65,70,70,75,90]
sns.histplot(data=marks,bins=5,kde=True)
plt.xlabel('Marks')
plt.ylabel('Density')
plt.title('DensityDistribution of Student Marks')
plt.show()