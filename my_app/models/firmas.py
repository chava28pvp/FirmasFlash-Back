from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from datetime import datetime
from sqlalchemy.orm import relationship
from my_app.main import Base


class firmas(Base):
    __tablename__ = 'Firma'

    id = Column('idFirma', Integer, primary_key=True)
    name = Column('Name', String)
    description = Column('Description', String)
    active = Column('Active', Integer, default=1)
    upload_by = Column('UploadBy', String)
    type_archive_id = Column('TypeArchive_Id', Integer, ForeignKey('TypeArchivo.idTypeArchive'))

    type_archive = relationship("typeArchive", back_populates="firmas")
    archive_urls = relationship("archiveURL", back_populates="firmas")


class archiveURL(Base):
    __tablename__ = 'ArchiveURL'

    id = Column('IdArchiveURL', Integer, primary_key=True)
    path_file = Column('pathFile', String)
    firma_id = Column('FirmaId', Integer, ForeignKey('Firma.idFirma'))  # CORREGIDO

    firma = relationship("firmas", back_populates="archive_urls")  # CORREGIDO


class typeArchive(Base):
    __tablename__ = 'TypeArchivo'

    id = Column('idTypeArchive', Integer, primary_key=True)
    description = Column('Description', String)
    creation_date = Column('CreationDate', DateTime, default=datetime.utcnow())

    # Relación inversa
    firmas = relationship("firmas", back_populates="typeArchive")


class usersAsignados(Base):
    __tablename__ = 'UsersAsignados'

    id = Column('IdUser', Integer, primary_key=True)
    id_Firma = Column('IdFirma', Integer, ForeignKey('Firma.idFirma'))
    usuario = Column('Usuario', String)

    firmas = relationship("firmas", back_populates="usersAsignados")

