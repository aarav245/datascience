import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("Titanic.csv")
pclass_counts = df["Pclass"].value_counts().sort_index()
x = [2,5,8]
plt.bar(x, pclass_counts.values, width = 1, color = "green")

for i in range(len(x)):
    plt.text(
        x[i],
        pclass_counts.values[i] + 5,
        str(pclass_counts.values[i]),
        ha = "center"
    )
plt.xticks(x, ["Class 1", "Class 2", "Class 3"])
plt.title("Passenger class distribution")
plt.xlabel("Class")
plt.ylabel("Passenger count")

plt.show()

#age graph

age_counts = (
    df["Age"].dropna().astype(int).value_counts().sort_values(ascending=False).head(10)
)

plt.bar(age_counts.index.astype(str), age_counts.values, color = "orange")
plt.title("Most common ages")
plt.xlabel("Age")
plt.ylabel("Passengers")
plt.show()