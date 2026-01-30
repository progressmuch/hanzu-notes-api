from sqlalchemy import Column, String, Integer, TIMESTAMP
from .database import Base
from sqlalchemy.sql.expression import text



class Notes(Base):
    __tablename__ = 'notesList'
    noteId = Column(Integer, nullable=False, primary_key=True)
    note = Column(String , nullable=False)
    created_at = Column(TIMESTAMP(timezone=True), server_default = text('now()'))
