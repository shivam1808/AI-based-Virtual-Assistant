import imdb
from colorama import Fore

app = imdb.IMDb()
movie = "war"
results = app.search_movie(movie, results=10)
first = results[0]
data = first.movieID
print(first.movieID)

print(app.get_movie(first.movieID))

print(data['year'])
