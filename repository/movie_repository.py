from typing import List
from copy import deepcopy

from exceptions.movie_not_found_exception import MovieNotFoundException
from repository.repository import Repository
from model.movie import Movie


class MovieRepository(Repository):
    movies = [
        Movie(
            id=1, type="movie", primary_title="Den sorte familie", original_title="Den sorte familie", release_year=1914
        ),
        Movie(
            id=2, type="short", primary_title="The Spanish Parrot Girl", original_title="The Spanish Parrot Girl",
            release_year=1913, genres=["Drama", "Romance", "Short"]
        ),
        Movie(
            id=3, type="short", primary_title="Blacksmith Scene", original_title="Les forgerons", release_year=1895,
            runtime=1, genres=["Documentary", "Short"]
        ),
        Movie(
            id=4, type="short", primary_title="The Sea", original_title="Baignade en mer", release_year=1895, runtime=1,
            genres=["Documentary", "Short"]
        ),
    ]

    def create(self, movie: Movie) -> None:
        self.movies.append(movie)

    def get_all(self) -> List[Movie]:  # semnul '->' inseamna Return
        return deepcopy(self.movies)

    def update(self, movie) -> None:
        for i, existing_movie in enumerate(self.movies):
            if movie.primary_title == existing_movie.primary_title:
                self.movies[i] = movie
                return
        raise MovieNotFoundException(f'Filmul nu a fost gasit {movie.primary_title}')

    def delete(self, title: str) -> Movie:
        for i, existing_movie in enumerate(self.movies):
            if title == existing_movie.primary_title:
                return self.movies.pop(i)
        raise MovieNotFoundException(f'Filmul nu a fost gasit {title}')

    def get_by_title(self, title):
        for movie in self.movies:
            if movie.primary_title == title:
                return movie
        raise MovieNotFoundException(f'Nu ti-am gasit filmul {title}')