import pandas as pd
data = pd.read_csv("mymoviedb.csv", engine = "python", on_bad_lines = "skip")

#convert columns into numerical values

data["Vote_Average"] = pd.to_numeric(data["Vote_Average"], errors = "coerce")
data["Vote_Count"] = pd.to_numeric(data["Vote_Count"], errors = "coerce")

print(data.head())
print(data.info())
print(data.dtypes)

#Multiple columns
tandG = data[["Title", "Genre"]]
print(tandG.head())
print(tandG.shape)

#Movie avg > 7

above7 = data[data["Vote_Average"] > 7]
print(above7[["Title", "Vote_Average"]].head())
print(above7.shape)

#movies in korean and english
engandKo = data[data["Original_Language"].isin(["en", "ko"])]
print(engandKo[["Title", "Original_Language"]].head())
print(engandKo.shape)

#movies in hindi or english

engandhindi = data[(data["Original_Language"]== "en") | (data["Original_Language"] == "hi")]
print(engandhindi[["Title","Original_Language"]].head())
print(engandhindi.shape)

#movies in english and vote avg is > 7

engandgreat7 = data[(data["Original_Language"]== "en") & (data["Vote_Average"] > 7)]
print(engandgreat7[["Title","Original_Language","Vote_Average","Popularity"]].head())
print(engandgreat7.shape)

englishmovies = data[(data["Original_Language"] == "en")&(data["Vote_Average"] > 7)]
koreanmovies = data[(data["Original_Language"] == "ko")&(data["Vote_Average"] > 7)]
japanesemovies = data[(data["Original_Language"] == "ja")&(data["Vote_Average"] > 7)]
frenchmovies = data[(data["Original_Language"] == "fr")&(data["Vote_Average"] > 7)]
hindimovies = data[(data["Original_Language"] == "hi")&(data["Vote_Average"] > 7)]

print("English Movies: ", englishmovies["Popularity"].mean())
print("Korean Movies: ", koreanmovies["Popularity"].mean())
print("Japanese Movies: ", japanesemovies["Popularity"].mean())
print("French Movies: ", frenchmovies["Popularity"].mean())
print("Hindi Movies: ", hindimovies["Popularity"].mean())