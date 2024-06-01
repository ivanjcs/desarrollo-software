from typing import List
from app.models import Movie
from app.repositories import MovieRepository
from app.services import Security

repository = MovieRepository()

class MovieService:
    
    """ Clase que se encarga de CRUD de Movies """
    def save(self, movie: Movie) -> Movie:
        #movie.password = Security.generate_password(movie.password) ????????? wtf
        return repository.save(movie)

    def update(self, movie: Movie, id: int) -> Movie:
        return repository.update(movie, id)
    
    def delete(self, movie: Movie) -> None:
        repository.delete(movie)

    def all(self) -> List[Movie]:
        return repository.all()
    
    def find(self, id: int) -> Movie:
        return repository.find(id)
    
    def find_by_name(self, name: str):
        return repository.find_by_name(name)
    
    # agregar más formas de encontrar peliculas

