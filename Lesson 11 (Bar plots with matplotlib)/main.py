import matplotlib.pyplot as plt

students = ["Aarav", "Elise", "Alex", "Emily", "Emma"]
marks = [80, 92, 87, 75, 78]

plt.bar(students, marks, color = "green")
plt.show()

#fruits

fruits = ["Apple", "Banana", "Orange", "Mango"]
quantity = [25,40,18,30]
plt.bar(fruits,quantity)
plt.title("Fruit sales")
plt.xlabel("fruits")
plt.ylabel("quantity sold")
plt.show()

#horizontal bar plot

languages = ["python", "java", "c++", "javascript"]
students = [50,35,25,40]
colors = ["red", "blue", "green", "orange"]
plt.barh(languages,students, color = colors)
plt.title("programming language popularity")
plt.show()

#student attendance

days = ["Mon", "tues", "wed", "thur", "fri"]
attendance = [25,28,30,27, 29]

plt.barh(days, attendance)
plt.title("student attendance")
plt.show()

#daily rainfall

days = ["Mon", "tues", "wed", "thur", "fri", "sat", "sun"]
rainfall = [12, 18, 25, 13, 14, 10, 14]

plt.bar(days, rainfall, color = "skyblue")
plt.title("daily rainfall")
plt.ylabel("rainfall (mm)")
plt.show()