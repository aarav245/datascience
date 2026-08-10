import matplotlib.pyplot as plt

fig, axes = plt.subplots(2,2)

axes[0,0].plot([1,2,3,4],[10,20,15,25])
axes[0,0].set_title("Line Plot")

axes[0,1].bar(["A", "B", "C"],[10,20,15])
axes[0,1].set_title("Bar chart")

axes[1,0].hist([10,11,12,12,13,14,15])
axes[1,0].set_title("Histogram")

axes[1,1].scatter([1,2,3,4],[20,30,25,40])
axes[1,1].set_title("Scatter plot")

plt.tight_layout()
plt.show()