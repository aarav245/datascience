import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from pandas.plotting import scatter_matrix

salarydataset = pd.read_csv("adult.csv")

salarydataset.columns = ["age","workclass","fnlwgt","education","educational-num","marital-status","occupation","relationship","race","gender","capital-gain","capital-loss",'hours-per-week','native-country','income']
salarydataset.rename(columns={"capital-gain":"capital gain","capital-loss":"capital loss","native-country":"country","hours-per-week":"hours worked", "marital-status":"married"},inplace=True)

print(salarydataset.describe())
print(salarydataset.info())
print(salarydataset.isnull().sum())
print(salarydataset.isin(["?"]).sum(axis = 0))

for c in salarydataset.columns:
    print("----%s----" % c)
    print(salarydataset[c].value_counts())

salarydataset.drop(
    [
        "educational-num",
        "age",
        "hours worked",
        "fnlwgt",
        "capital gain",
        "capital loss",
        "country"
    ],
    axis = 1,
    inplace=True
)
income = set(salarydataset["income"])
print(income)

income = set(salarydataset["income"])
print(income)

salarydataset["income"] = (
    salarydataset["income"].map({" <=50K" :0," >50K":1}).astype(int)
)

salarydataset["gender"] = (
    salarydataset["gender"].map({" Male":0, " Female":1}).astype(int)
)

salarydataset["race"] = (
    salarydataset["race"].map(
        {
            " Black":0,
            " Asian-Pac-Islander":1,
            " Other":2,
            " White":3,
            " Amer-Indian-Eskimo":4
        }
    ).astype(int)
)

salarydataset["married"] = (
    salarydataset["married"].map(
        {
            " Married-spouse-absent":0,
            " Widowed":1,
            " Married-civ-spouse":2,
            " Seperated":3,
            " Divorced":4,
            " Never-married":5,
            " Married-AF-spouse":6
        }
    ).astype(int)
)

salarydataset["relationship"] = (
    salarydataset["relationship"].map(
        {
            " Not-in-family":0,
            " Wife":1,
            " Other-relative":2,
            " Unmarried":3,
            " Husband":4,
            " Own-child":5,
        }
    ).astype(int)
)

salarydataset.groupby("education").income.mean().plot(ind = "bar")
plt.show()

salarydataset.groupby("occupation").income.mean().plot(ind = "bar")
plt.show()

salarydataset.groupby("relationship").income.mean().plot(ind = "bar")
plt.show()

salarydataset.groupby("race").income.mean().plot(ind = "bar")
plt.show()

salarydataset.groupby("gender").income.mean().plot(ind = "bar")
plt.show()

salarydataset.groupby("workclass").income.mean().plot(ind = "bar")
plt. show()

salarydataset.groupby("married").income.mean().plot(ind = "bar")
plt.show()