import matplotlib.pyplot as plt
fig,ax=plt.subplots(1,2) # 1row, 2 columns\
ax[0].plot([1,2,3],[10,20,30])  # first chart
ax[0].set_title("Chart1")
ax[1].bar(["A","B","C"],[30,20,40])  # second chart
ax[1].set_title("Chart2")
plt.show()