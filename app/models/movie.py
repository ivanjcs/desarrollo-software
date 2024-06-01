from dataclasses import dataclass
from typing import List
from app import db
from app.models.relations import users_roles


@dataclass(init=False, repr=True, eq=True)
class Movie(db.Model):
    __tablename__ = 'movies'
    id: int = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name: str = db.Column(db.String(80), nullable=False)
    director: str = db.Column(db.String(80), nullable=False)
    year: int = db.Column(db.Integer, nullable=False)
    start_date: str = db.Column(db.String(80), nullable=False)
    final_date: str = db.Column(db.String(80))
    duration: int = db.Column(db.Integer, nullable=False)
    description: str = db.Column(db.String(80), nullable=False)
    genre: str = db.Column(db.String(80), nullable=False)
    classification: str = db.Column(db.String(80), nullable=False)
    cast: str = db.Column(db.String(80), nullable=False)
    language: str = db.Column(db.String(80), nullable=False)
    
    # FALTAN RELACIONES
    