import pandas as pd

data = {
    'Names':["James","Elizabeth","Grace","Jonathan","Oliver","Henry"],
    'Math':[85,68,92,81,73,78],
    'English':[75,81,83,87,91,72],
    'Science':[89,94,97,93,88,95]
}
df = pd.DataFrame(data)
print(df)
highest = df.max()
print(highest)
lowest = df.min()
print(lowest)
meanmath = df["Math"].mean()
print(meanmath)
meaneng = df["English"].mean()
print(meaneng)
meanscience = df["Science"].mean()
print(meanscience)
above75math = df["Math"] > 75
print(above75math)