import matplotlib.pyplot as plt
students=["A","B","C","D"]
marks=[70,85,60,95]
fig,ax=plt.subplots()
ax.plot(students,marks)
ax.set_xlabel("Students")
ax.set_ylabel("Marks")
plt.show()