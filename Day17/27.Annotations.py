import matplotlib.pyplot as plt
months=[1,2,3,4]
sales=[100,200,150,300]
fig,ax=plt.subplots()
ax.plot(months,sales,marker="o")
ax.annotate(
    "Highest Sales",xy=(4,300),xytext=(2,300),
arrowprops=dict(arrowstyle="->",color="red"),fontsize=18,color="purple")
plt.show()