import matplotlib.pyplot as plt

#scatter plot
studyhours = [1,2,3,4,5,6]
scores = [40,45,55,65,70,85]
plt.scatter(studyhours,scores)
plt.title("Study Hours vs exam scores")
plt.xlabel("Study hours")
plt.ylabel("Exam scores")
plt.show()

#histogram
ages = [10,11,12,12,13,13,13,14,14,15,15,16,17]
plt.hist(ages, bins = 5)
plt.title("Student ages")
plt.xlabel("Age")
plt.ylabel("# of students")
plt.show()

#pie chart
activities = ["Study", "Sleep", "Play", "Other"]
hours = [6,8,3,7]
plt.pie(hours, labels=activities, shadow=True, autopct="%1.1f%%")
plt.title("Daily activities")
plt.show()

#stack plot
days = ["Mon", "Tue", "Wed", "Thu", "Fri"]
sleeping = [8,8,7,8,7]
eating = [2,2,2,2,2]
working = [8,7,8,7,8]
playing = [2,3,3,3,3]
plt.stackplot(
    days,
    sleeping,
    eating,
    working,
    playing,
    labels = ["Sleeping", "Eating", "Working", "Playing"]
)
plt.title("Daily Activities")
plt.xlabel("days")
plt.ylabel("hours")
plt.legend()
plt.show()