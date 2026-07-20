import pandas as pd
data = pd.read_csv("iris.csv")

minsepal_length = data.loc[data["sepal_length"] > 4, ["sepal_length","species"]]
print(minsepal_length.head())

#index slicing

print(data.iloc[3:5,1:3].head())
data.loc[0:1, "species"] = "newspecies" 
print(data["species"]) 


#new column

data["NewSepalLength"] = data["sepal_length"] + 2
print(data["NewSepalLength"].head())
data["Newcolumn"] = data["NewSepalLength"]
print(data["Newcolumn"])
data.to_csv("Edited.csv")