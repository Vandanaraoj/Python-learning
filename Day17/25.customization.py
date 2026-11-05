import matplotlib.pyplot as plt
students=["A","B","C","D"]
marks=[70,85,60,95]
fig,ax=plt.subplots()
ax.plot(students,marks)
ax.set_title("Student performance")
ax.set_title("Student performance",fontsize=16,color="blue")
ax.set_xlabel("Students",fontsize=14)
ax.set_ylabel("Marks",fontsize=12)
ax.legend()
plt.show()