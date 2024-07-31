
from flask import Blueprint, request
from app.mapping import ResponseSchema, MovieSchema
from app.services.response_message import ResponseBuilder
from app.services.movie_services import MovieService

movie = Blueprint('movie', __name__)
movie_schema = MovieSchema()
response_schema = ResponseSchema()
movie_service = MovieService()

@movie.route('/movies', methods=['GET'])
def index():
    return {"movies": movie_schema.dump(movie_service.all(),many=True)}, 200