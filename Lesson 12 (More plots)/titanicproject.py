import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("titanic.csv")
print(df.head())
print("\nNumber of Passengers: ", len(df))
print("\n columns:")
print(df.columns)
plt.figure(figsize = (14,10))

#Bar chart, number of survivors vs non

plt.subplot(2,3,1)

survival_counts = df["Survived"].value_counts()
plt.bar(
    ["Did not survive", "Survived"],
    [survival_counts.get(0,0), survival_counts.get(1,0)]
)
plt.title("Titanic survivors")
plt.xlabel("Survival status")
plt.ylabel("# of survivors")

#Pie chart, Survival percentage

plt.subplot(2,3,2)
survival_counts = df["Survived"].value_counts()
plt.pie(
    survival_counts,
    labels = ["Didn't survive", "Survived"],
    autopct = "%1.1f%%",
    startangle= 90

)
plt.title("Survival %")

#histogram, distribution of passanger ages

plt.subplot(2,3,3)
plt.hist(df["Age"].dropna(), bins = 10)

plt.title("Age Distribution")
plt.xlabel("Age")
plt.ylabel("# of passengers")

#Scatter plot, Age versus fair

plt.subplot(2,3,4)

age_fare = df[["Age", "Fare"]].dropna()
plt.scatter(age_fare["Age"], age_fare["Fare"])

plt.title("Age versus fare")
plt.xlabel("Age")
plt.ylabel("Fare")

#Line plot, passengers in each class

plt.subplot(2,3,5)

class_counts = df["Pclass"].value_counts().sort_index()

plt.plot(class_counts.index, class_counts.values, marker = "o")
plt.title("Passengers by class")
plt.xlabel("Passenger class")
plt.ylabel("# of passengers")

#Stack Plot, Male Vs Female by Pclass

plt.subplot(2,3,6)
class_numbers = [1,2,3]

male_counts = []
female_counts = []

for pclass in class_numbers:
    class_data = df[df["Pclass"] == pclass]
    male_counts.append(len(class_data[class_data["Sex"] == "male"]))
    female_counts.append(len(class_data[class_data["Sex"] == "female"]))

plt.stackplot(class_numbers, male_counts, female_counts, labels=["Male", "Female"])
plt.title("Gender distribution by class")
plt.xlabel("Passenger class")
plt.ylabel("# of passengers")

plt.legend()

plt.tight_layout()
plt.show()

print("TITANIC DATA ANALYSIS")
print("\n Total passengers: ", len(df))

survived = df["Survived"].sum()
print("Total survived: ", survived)

deaths = len(df) - survived
print("Total deaths: ", deaths)

survivalpercent = (survived/len(df)) * 100
print("Survival percentage", round(survivalpercent, 2), "%")

average_age = df["Age"].mean()
print("Average age: ", round(average_age, 2))

most_common = df["Pclass"].mode()[0]
print("Most common Passenger class: ", most_common)

maxfare = df["Fare"].max()
print("Highest fare: ", maxfare)