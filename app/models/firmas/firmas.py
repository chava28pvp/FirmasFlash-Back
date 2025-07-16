from sqlalchemy import Column, Integer, String
from app.db.database import db_manager

Base = db_manager.get_base('primary')

class firmas(Base):
    __tablename__ = 'Firma'

    idFirma = Column(Integer, primary_key=True)
    Name = Column(String, unique=False)
    Description = Column(String, unique=False)
    Active = Column(Integer, unique=False)
    UploadBy = Column(String, unique=False)
    TypeArchive_Id = Column(Integer, unique=False)
