import pandas as pd
data = pd.read_csv("music_streaming_habits_2026.csv", engine = "python", on_bad_lines = "skip")
data["age"] = pd.to_numeric(data["age"],errors = "coerce")
print(data.head())
print(data.info())
print(data.dtypes)
candage = data[["country","age"]]
print(candage)
print(candage.shape)