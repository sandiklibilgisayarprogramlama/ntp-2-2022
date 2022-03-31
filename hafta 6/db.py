from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey, Text
from sqlalchemy import create_engine
engine = create_engine('sqlite:///veritabani.db', echo=True)

Base = declarative_base()


class Ogrenci(Base):
    __tablename__ = 'ogrenci'
    id = Column(Integer, primary_key=True)

    ad = Column(String)
    soyad = Column(String)
    email = Column(String)


class Adres(Base):
    __tablename__ = "adres"

    id = Column(Integer, primary_key=True)
    ogrenci_id = Column(Integer, ForeignKey("ogrenci.id"))
    acikadres = Column(Text)


Base.metadata.create_all(engine)
