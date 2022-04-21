#oturum = Session()

# 1. session.query(Ogrenci).get(2)

# 2. session.query(Ogrenci).
# filter(_and(ad=="cemal",soyad=="elvan"))
"""
ogrenci = session.query(Ogrenci).filter(ad==ismail)
ogrenci.eposta = "ismail@gmail.com"
ogrenci.commit()


ogrenci = session.query(ogrenci).filter(soyad=="cenk")
session.delete(ogrenci)
"""

# session.query(ogrenci).count()
