from dataclasses import dataclass
from app import db

@dataclass(init=False, repr=True, eq=True)
class Ticket(db.Model):
    __tablename__ = 'tickets'
    id: int = db.Column(db.Integer, primary_key=True, autoincrement=True)
    movie: str = db.Column(db.String(80), nullable=False)
    price: int = db.Column(db.Integer, nullable=False)
    date: str = db.Column(db.String(80), nullable=False)
    hour: int = db.Column(db.Integer, nullable=False)