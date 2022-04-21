from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey, Text
from sqlalchemy import create_engine
engine = create_engine('sqlite:///veritabani.db', echo=True)
Base = declarative_base()


class Kullanici(Base):
    __tablename__ = 'kullanici'
    id = Column(Integer, primary_key=True)
    kullaniciadi = Column(String)
    sifre = Column(String)
    ad = Column(String)


Base.metadata.create_all(engine)
