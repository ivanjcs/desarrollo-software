from dataclasses import dataclass
from app.models.audit_mixin import AuditMixin
from app.models.soft_delete import SoftDeleteMixin
from app import db

@dataclass(init=False, repr=True, eq=True)
class Room(SoftDeleteMixin, AuditMixin,db.Model):
    __tablename__ = 'rooms'
    id: int = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name: str = db.Column(db.String(80), unique=True, nullable=False)
    number: int = db.Column(db.Integer, nullable=False)
    seatsnumber: int = db.Column(db.Integer, nullable=False)