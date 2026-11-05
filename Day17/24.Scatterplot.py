import matplotlib.pyplot as plt
sleep=[1,2,3,4,5]
marks=[35,45,55,70,85]
fig,ax=plt.subplots()
ax.scatter(sleep,marks)
ax.set_title(" Sleep vs Marks")
ax.set_xlabel("Sleep")
ax.set_ylabel("Marks")
plt.show()