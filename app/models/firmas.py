from sqlalchemy import Column, Integer, String, DateTime, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from .base import BaseModel


class firmas(BaseModel):
    __tablename__ = 'Firma'

    id = Column('idFirma', Integer, primary_key=True)  # Mejor usar 'id' como estándar
    name = Column('Name', String)  # Longitud máxima recomendada
    description = Column('Description', String)
    active = Column('Active', Boolean, default=True)  # Boolean es más semántico
    upload_by = Column('UploadBy', String)
    type_archive_id = Column('TypeArchive_Id', Integer, ForeignKey('type_archives.id'))  # Relación

    # Relaciones
    type_archive = relationship("TypeArchive", back_populates="firmas")
    archive_urls = relationship("ArchiveURL", back_populates="firma")


class archiveURL(BaseModel):
    __tablename__ = 'ArchiveURL'

    id = Column('IdArchiveURL', Integer, primary_key=True)
    path_file = Column('pathFile', String)  # Ruta puede ser larga
    firma_id = Column('FirmaId', Integer, ForeignKey('firmas.id'))  # Relación

    # Relación inversa
    firma = relationship("Firma", back_populates="archive_urls")


class typeArchive(BaseModel):
    __tablename__ = 'TypeArchive'

    id = Column('idTypeArchive', Integer, primary_key=True)
    description = Column('Description', String)
    creation_date = Column('CreationDate', DateTime)

    # Relación inversa
    firmas = relationship("Firma", back_populates="type_archive")