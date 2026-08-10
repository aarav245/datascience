import matplotlib.pyplot as plt

x = [1,2,3,4,5]
y = [10,20,15,25,30]

products = ["a", "b", "c", "d"]
sales = [40,60,30,80]
ages = [10,11,12,12,13,13,13,14,14,15,15]
studyhrs = [1,2,3,4,5]
scores = [40,50,60,75,90]

#line plot
plt.subplot(2,2,1)
plt.plot(x,y)
plt.title("Line plot")
plt.xlabel("x")
plt.ylabel("y")

#bar graph
plt.subplot(2,2,2)
plt.bar(products,sales)
plt.title("Bar chart")
plt.xlabel("products")
plt.ylabel("sales")

#histogram
plt.subplot(2,2,3)
plt.hist(ages,bins = 5, histtype="bar")
plt.title("Histogram")
plt.xlabel("Ages")
plt.ylabel("frequency")

#scatter plot
plt.subplot(2,2,4)
plt.scatter(studyhrs, scores)
plt.title("scatter plot")
plt.xlabel("study hours")
plt.ylabel("scores")

plt.tight_layout()
plt.show()