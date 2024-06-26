from dataclasses import dataclass
from datetime import datetime,timedelta

from app import db
from sqlalchemy import Column, DateTime

@dataclass(init=False,repr=True, eq=True)
class Feature(db.Model):
    __tablename__ = 'features'
    id: int = db.Column(db.Integer, primary_key=True, autoincrement=True)
    date_from: str = Column(DateTime, nullable=False, default=datetime.now())
    date_to: str = Column(DateTime, nullable=False, deafult=datetime.now()+timedelta(days=2))
    
    # FALTAN RELACIONES