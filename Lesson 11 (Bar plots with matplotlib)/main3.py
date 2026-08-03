#student performance dashboard
import matplotlib.pyplot as plt

students = ["Aarav", "Elise", "Amelie", "Alex", "David"]
math = [85, 92, 78, 88, 90]
science = [90, 89, 80, 91, 84]
x = [0,1,2,3,4]
width = .35
plt.figure(figsize = (8,5))
plt.bar(x, math, width=width, label = "Math", color = "royalblue")
plt.bar([i+width for i in x], science, width=width, label = "science", color = "orange")
plt.xticks([i + width / 2 for i in x], students)
plt.title("Student performances")
plt.xlabel("students")
plt.ylabel("Marks")
plt.grid(axis = "y", linestyle = "--")
plt.legend()
plt.show()

#sorted bar plot

countries = ["India", "USA", "China", "Japan", "Germany"]
gdp = [3.9,29.1,18.5,4.2,4.7]
data = list(zip(countries,gdp))
data.sort(key = lambda x: x[1], reverse = True)
countries = [i[0] for i in data]
gdp = [i[1] for i in data]
plt.bar(countries,gdp)
plt.title("GDP comparison")
plt.ylabel("Trillion dollars")
plt.show()