from model.movie import Movie
from repository.movie_repository import MovieRepository

new_movie = Movie(id=5, type="movie", primary_title="Harry Potter", original_title="Harry Potter", release_year=2001,
                  genres=["Adventure"])

repo = MovieRepository()
all_movies = repo.get_all()
print(all_movies)
repo.create(new_movie)
all_movies = repo.get_all()
print(all_movies)

new_movie.genres.append('Family')
print(all_movies)

repo.update(new_movie)

all_movies = repo.get_all()
print(all_movies)

repo.get_all()
print(all_movies)

print(repo.delete('Harry Potter'))
