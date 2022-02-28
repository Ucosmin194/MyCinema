from exceptions.movie_not_found_exception import MovieNotFoundException


class MovieRepository:
    filme = [{
        'name': 'Harry Potter 1',
        'year': 2001
    },
        {
            'name': 'Harry Potter 2',
            'year': 2002
        },
        {
            'name': 'Harry Potter 3',
            'year': 2004
        }]

    def get_by_name(self, name):
        for film in self.filme:
            if film['name'] == name:
                return film
        raise MovieNotFoundException(f'Nu am gasit filmul {name}')


repo = MovieRepository()
try:
    repo.get_by_name('Harry Potter 7')
except MovieNotFoundException as ex:
    print(ex)
except (FileNotFoundError, FileExistsError):
    print('Nu exista fisierul')
except:
    print('Alta eroare s-a intamplat')
