import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

data = pd.read_csv("titanic.csv")
data.columns = data.columns.str.strip()
print("Columns: ")
print(data.columns.tolist())
print("\n first 5 rows: ")
print(data.head())

print("\nMissing values bhefore preprocessing")
print(data.isnull().sum())

avgage = data["Age"].mean()
print("Average age: ", avgage)
data["Age"] = data["Age"].fillna(avgage)
if "Embarked" not in data.columns:
    print("Column was not found")
    print("Creating an embarked column with 'unknown'.")
    data["Embarked"] = 'unknown'

most_common_embarked = data["Embarked"].mode() [0]
print("\nMost common Embarked values: ", most_common_embarked)

data["Embarked"] = data["Embarked"].fillna(most_common_embarked)

data["Sex"] = data["Sex"].str.strip().str. lower()
data["Sex"] = data["Sex"].map({"male":0,"female":1})

data["Embarked"] = data["Embarked"].astype(str)
data["Embarked"] = data["Embarked"].str.strip(). str. lower()
data["Embarked"]=data["Embarked"].map({"S":0,"C":1,"Q":2,"UNKNOWN": 3})

print("\nData after preprocessing: ")
print(data.head())

print("\nMissing Vlues after preprocessing: ")
print(data.isnull().sum())

X = data[["Pclass", "Sex", "Fare", "Embarked"]]
Y = data["Survived"]
Xtrain, Xtest, Ytrain, Ytest = train_test_split(X,Y,test_size=.2,random_state=42)
print("\nTraining samples: ", len(Xtrain))
print("Testing samples: ",len(Xtest))

model = DecisionTreeClassifier(random_state=42)

model.fit(Xtrain, Ytrain)
print("\nModel Training Completed!")

predictions = model.predict(Xtest)

print("\nActual Values: ")
print(Ytest.head(10).values)

accuracy = accuracy_score(Ytest, predictions)
print("\nModel Accuracy:")
print(accuracy)

print("\nAccuracy Percentage")
print(round(accuracy *100,2),"%")

new_passenger = pd.DataFrame([[1, 1,25, 100,1]],columns = ["Pclass", "Sex", "Age", "Fare", "Embarked"])

new_prediction = model.predict(new_passenger)
print("\nNEW PASSENGER PREDICTION")

if new_prediction[0] == 1:
    print("The passenger is predicted to SURVIVE. ")
else:
    print("The passenger is predicted to NOT SURVIVE.")