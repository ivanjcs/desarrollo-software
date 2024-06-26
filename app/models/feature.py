from dataclasses import dataclass
from datetime import datetime,timedelta

from app import db
from sqlalchemy import Column, DateTime
from app.models.audit_mixin import AuditMixin
from app.models.soft_delete import SoftDeleteMixin

@dataclass(init=False,repr=True, eq=True)
class Feature(SoftDeleteMixin, AuditMixin,db.Model):
    __tablename__ = 'features'
    id: int = db.Column(db.Integer, primary_key=True, autoincrement=True)
    date_from: str = Column(DateTime, nullable=False, default=datetime.now())
    date_to: str = Column(DateTime, nullable=False, default=datetime.now()+timedelta(weeks=2))
    
    # FALTAN RELACIONES