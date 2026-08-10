import matplotlib.pyplot as plt

students = ["A","b","c","d","E"]
marks = [70,85,60,90,75]
studyhrs = [2,4,1,5,3]

#Line plot
plt.subplot(2,2,1)
plt.plot(students,marks, marker = "o")
plt.title("Student marks")
plt.xlabel("Students")
plt.ylabel("Marks")

#Bar chart
plt.subplot(2,2,2)
plt.bar(students,marks)
plt.title("Marks comparison")
plt.xlabel("students")
plt.ylabel("Marks")

#scatter plot
plt.subplot(2,2,3)
plt.scatter(studyhrs,marks)
plt.title("study hours vs marks")
plt.xlabel("study hours")
plt.ylabel("Marks")

#Pie chart
plt.subplot(2,2,4)
plt.pie(marks, labels=students, autopct= "%1.1f%%")
plt.title("marks distribution")

plt.tight_layout()
plt.show()