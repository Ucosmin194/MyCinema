from typing import List

from exceptions.movie_not_found_exception import MovieNotFoundException
from model.movie import Movie
from repository.repository import Repository


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

    def get_all(self) -> List[Movie]:
        return self.movies

    def update(self, movie) -> None:
        for i, existing_movie in enumerate(self.movies):
            if movie.primary_title == existing_movie.primary_title:
                self.movies[i] = movie
                return
        raise MovieNotFoundException(f'Nu am gasit filmul {movie.primary_title}')

    def delete(self, title: str):
        for i, existing_movie in enumerate(self.movies):
            if title == existing_movie.primary_title:
                return self.movies.pop(i)
        raise MovieNotFoundException(f'Nu am gasit filmul {title}')

    def create(self, movie: Movie) -> None:
        return self.movies.append(movie)

    def get_by_title(self, title):
        for movie in self.movies:
            if movie.primary_title == title:
                return movie
        raise MovieNotFoundException(f'Nu ti-am gasit filmul {title}')


repo = MovieRepository()
try:
    repo.get_by_title('Harry Potter 7')
except MovieNotFoundException as ex:
    print(ex)
except (FileNotFoundError, FileExistsError):
    print('Nu exista fisierul')
except:
    print('Alta eroare s-a intamplat')
