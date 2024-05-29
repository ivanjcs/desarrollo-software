from typing import List
from app.models import Movie
from app.repositories import MovieRepository
from app.services import Security

repository = MovieRepository()

class MovieService:
    
    """ Clase que se encarga de CRUD de Movies """
    