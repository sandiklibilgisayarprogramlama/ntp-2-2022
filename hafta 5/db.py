from sqlalchemy import create_engine, ForeignKey, MetaData, Table, Column, Integer, String
engine = create_engine('sqlite:///veritabani.db', echo=True)
meta = MetaData()

students = Table(
    'ogrenci', meta,
    Column('id', Integer, primary_key=True),
    Column('ad', String),
    Column('soyad', String),
    Column('yas', Integer),
)

addresses = Table("adres", meta,
                  Column("id", Integer, primary_key=True),
                  Column("ogrenci_id", Integer, ForeignKey("ogrenci.id")),
                  Column("acikadres", String))

meta.create_all(engine)

# create,alter sql işlemleri yapılacak.
