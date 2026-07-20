import pandas as pd

data = pd.read_csv("mymoviedb.csv", engine = "python", on_bad_lines="skip")
data["Vote_Average"] = pd.to_numeric(data["Vote_Average"], errors = "coerce")
data["Vote_Count"] = pd.to_numeric(data["Vote_Count"], errors = "coerce")
print("First 5 rows of the dataset: ")
print(data.head())

print("\n 5 to 9 for rows and columns 1 to 3: ")
print(data.iloc[5:10, 1:4])

print("\nMovies with vote average greater than 8: ")
print(data.loc[data["Vote_Average"] > 8, ["Title", "Vote_Average"]])

print("\nNumber of movies for each language: ")
print(data["Original_Language"].value_counts())

print("\nAverage Rating based on Language: ")
print(data.groupby("Original_Language")["Vote_Average"].mean())

print("\nAverage vote count based on language: ")
print(data.groupby("Original_Language")["Vote_Count"].mean())

print("\nAverage rating based on lanuyage and Genre: ")
print(data.groupby(["Original_Language", "Genre"])["Vote_Average"].mean())

print("\nMovie stats: ")
print(data.agg({"Popularity" : ["min","max","mean","median"],"Vote_Count" : ["min","max","mean","median"], "Vote_Average" : ["min","max","mean","median"]}))

print("\nMovies sorted by Vote average: ")
datasorted = data.sort_values(by = "Vote_Average", ascending=False)
print(datasorted[["Title", "Vote_Average"]].head(10))

print("\nMovies sorted by Popularity: ")
datasorted = data.sort_values(by = "Popularity", ascending=False)
print(datasorted[["Title", "Popularity"]].head(10))

data["Popularity+10"] = data["Popularity"] + 10
print("\nPopularity+10")
print(data[["Title","Popularity","Popularity+10"]].head())