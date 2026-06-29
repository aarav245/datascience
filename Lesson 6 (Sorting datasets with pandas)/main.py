import pandas as pd
data = pd.read_csv("titanic.csv")
print(data.info())
print(data.head())
print(data.dtypes)
nameandage = data[["Name","Age"]] 
print(nameandage)
print(nameandage.head())
print(nameandage.shape)
ageover = nameandage[nameandage['Age']> 35]
print(ageover.head())
print(ageover.shape)
classover = data[data["Pclass"].isin([2,3])]
print(classover[["Name","Pclass"]].head())
print(classover.shape)