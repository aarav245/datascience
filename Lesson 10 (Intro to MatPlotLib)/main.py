import matplotlib.pyplot as plt

x = [1,2,3,4,5]
y = [10,15,7,20,18]

plt.plot(x,y)
#plt.axis([0,6,0,50])
plt.xlim(0,6)
plt.ylim(0,60)
plt.show()

#Line plot w/ title and labels

months = ["Jan", "Feb", "Mar", "Apr", "May"]
sales = [100,120,140,130,170]
plt.plot(months, sales, color = "red", linestyle = "--", marker = "o", markersize = 10, linewidth = 2, label = "Sales")
plt.title("Monthly Sales")
#plt.xlabel("Months")
#plt.ylabel("Sales")
plt.legend()
plt.grid()
plt.show()

#multiple lines in graph

months = [1,2,3,4,5]
sales = [100,120,150,170,200]
profit = [20,25,35,40,45]
plt.plot(months, sales, label = "Sales")
plt.plot(months, sales, label = "Profit")
plt.legend()
plt.grid()
plt.show()
