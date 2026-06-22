import pandas as pd
data = {
    'Name':["James","Pablo","William","Mark","Ryan"],
    'Age':[10,12,15,17,13],
    'City':["Chicago","Los Angeles","New York City","San Antonio","Reno"]
}
df = pd.DataFrame(data)
print(df)
max = df.max()
print(max)
min = df.min()
print(min)
mean = df["Age"].mean()
print(mean)