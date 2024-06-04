from dataclasses import dataclass
from typing import List

#from app.models.audit_mixin import AuditMixin
#from app.models.soft_delete import SoftDeleteMixin
from app import db
from app.models.relations import users_roles
from app.models.audit_mixin import AuditMixin
from app.models.soft_delete import SoftDeleteMixin
from datetime import datetime,timedelta
from sqlalchemy import Column, DateTime

@dataclass(init=False, repr=True, eq=True)
class Movie(SoftDeleteMixin, AuditMixin,db.Model):
    __tablename__ = 'movies'
    id: int = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name: str = db.Column(db.String(80), nullable=False)
    director: str = db.Column(db.String(80), nullable=False)
    year: int = db.Column(db.Integer, nullable=False)
    start_date: str = Column(DateTime, nullable=False, default=datetime.now())
    final_date: str = Column(DateTime, nullable=False, default=datetime.now()+timedelta(weeks=2))
    duration: int = db.Column(db.Integer, nullable=False)
    description: str = db.Column(db.String(80), nullable=False)
    genre: str = db.Column(db.String(80), nullable=False)
    classification: str = db.Column(db.String(80), nullable=False)
    cast: str = db.Column(db.String(80), nullable=False)
    language: str = db.Column(db.String(80), nullable=False)
    
    # FALTAN RELACIONES
    