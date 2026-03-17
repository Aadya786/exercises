import json

with open("dataset.json", "r") as file:
    movies = json.load(file)

top_movies = [movie for movie in movies if movie["rating"] > 8.0]

with open("top_movies.json", "w") as outfile:
    json.dump(top_movies, outfile, indent=4)

print("Top movies saved to top_movies.json:")
for m in top_movies:
    print(f"{m['title']} ({m['rating']})")
