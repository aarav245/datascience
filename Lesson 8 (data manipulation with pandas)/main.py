import pandas as pd
data = pd.read_csv("titanic.csv")

anames = data.loc[data["Age"] > 18, ["Name","Age"]]
print(anames.head())

#index slicing

print(data.iloc[9:25,2:5].head())
data.iloc[0:3,2] = "Aarav"
print(data["Name"])


#new column

data["NewFare"] = data["Fare"] + 2
print(data["NewFare"].head())
data["Newcolumn"] = data["Fare"] * data["Pclass"]
print(data["Newcolumn"])
data.to_csv("Edited.csv")