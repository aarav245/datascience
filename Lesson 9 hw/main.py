import pandas as pd

data = pd.read_csv("iris.csv", engine = "python", on_bad_lines="skip")
data["sepal_length"] = pd.to_numeric(data["sepal_length"], errors = "coerce")
data["sepal_width"] = pd.to_numeric(data["sepal_width"], errors = "coerce")
data["petal_length"] = pd.to_numeric(data["petal_length"], errors = "coerce")
data["petal_width"] = pd.to_numeric(data["petal_width"], errors = "coerce")
print("First 5 rows: ")
print(data.head())

print("\n rows 3-8 and columns 2-4: ")
print(data.iloc[3:9, 2:5])

print("\n plants with petal length greater than 1.2: ")
print(data.loc[data["petal_length"] > 1.2, ["species", "petal_length"]])

print("\n Number of species: ")
print(data["species"].value_counts())

print('\n Average length of sepal based on species: ')
print(data.groupby("species")["sepal_length"].mean())

print("\n Species statistics: ")
print(data.agg({"sepal_length" : ["min", "max", "mean", "median"], "sepal_width" : ["min", "max", "mean", "median"], "petal_length" : ["min", "max", "mean", "median"], "petal_width" : ["min", "max", "mean", "median"]}))



