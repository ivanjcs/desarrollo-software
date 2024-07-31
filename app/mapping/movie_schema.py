from app.models.user import User
from marshmallow import validate, fields, Schema, post_load

class MovieSchema(Schema):
    id = fields.Integer(dump_only=True)
    name = fields.String(required=True)
    director = fields.String(required=True)
    year = fields.Integer(required=True)
    start_date = fields.DateTime(required=True)
    final_date = fields.DateTime(required=True)
    duration = fields.Integer(required=True)
    description = fields.String(required=True)
    genre = fields.String(required=True)
    classification = fields.String(required=True)
