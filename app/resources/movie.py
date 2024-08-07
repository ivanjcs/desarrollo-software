
from flask import Blueprint, request
from app.mapping import ResponseSchema, MovieSchema
from app.services.response_message import ResponseBuilder
from app.services.movie_services import MovieService

movie = Blueprint('movie', __name__)
movie_schema = MovieSchema()
response_schema = ResponseSchema()
movie_service = MovieService()

# Muestra todas las peliculas
@movie.route('/movies', methods=['GET'])
def index():
    return {"movies": movie_schema.dump(movie_service.all(),many=True)}, 200 #, 200 es el código de respuesta si todo funciona bien

#Añadir peliculas
@movie.route('/movies/add', methods=['POST'])
def post_movie():
    movie = movie_schema.load(request.json)
    return {"movie": movie_schema.dump(movie_service.save(movie))}, 201

#@movie.route('/movies/<int:id>', methods=['GET'])
#def find(id:int):
#    response_builder = ResponseBuilder()
#    response_builder.add_message("Pelicula encontrada").add_status_code(100).add_data(movie_schema.dump(movie_schema.find(id)))
#    return response_schema.dump(response_builder.build()), 200