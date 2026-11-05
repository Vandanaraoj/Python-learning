import matplotlib.pyplot as plt
months=[1,2,3,4]
shop_a=[100,200,150,300]
shop_b=[150,180,250,350]
fig,ax=plt.subplots()
ax.plot(months,shop_a,label="Shop A")
ax.plot(months,shop_b,label="Shop B")
ax.set_title("Shop Sales comparison")
ax.set_xlabel("Months")
ax.set_ylabel("Sales")
ax.set_yticks([150,237])
ax.set_xticks([1,5,8,10])
ax.tick_params(axis="both",labelsize=15)
ax.grid(True,alpha=0.3)
ax.legend()
plt.show()
