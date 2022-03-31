from ntpath import join
from db import Adres, Ogrenci, engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import and_, or_

Session = sessionmaker(bind=engine)

oturum = Session()
"""
nesne = Ogrenci(ad="Ahmet", soyad="uzun", email="deneme@deneme.com")
nesne2 = Ogrenci(ad="Veli", soyad="uzun2", email="den2eme@deneme.com")

# ret = oturum.add(nesne) # tek insert
oturum.add_all([nesne, nesne2])  # birden fazla insert işlemi gerçekleştir.
oturum.commit()

ogrenci = Ogrenci(ad="Hasan", soyad="uzun", email="d@dad.com")
oturum.add(ogrenci)
oturum.commit()
# sqlachemy eklenen ogrencinin id'sini otomatik olarak ogrenci nesnesinin
# id'sine atıyor. (kendisi güncelliyor)

adres = Adres(ogrenci_id=ogrenci.id, acikadres="Afyon")
oturum.add(adres)
oturum.commit()
"""
# Tablodaki tüm veriyi cekme
ogrenciler = oturum.query(Ogrenci).all()
for o in ogrenciler:
    print(o.ad + " "+o.soyad+" "+o.email)

# tablodaki ilk veriyi çekme
ilk_kayit = oturum.query(Ogrenci).first()
print(ilk_kayit.ad)

# id' ye göre veri çekme
id_ye_gore_cekme = oturum.query(Adres).get(3)
print(id_ye_gore_cekme.acikadres)

# id değerine göre filtreleme
filtre_sonuc = oturum.query(Adres).filter(Adres.id > 2)
for k in filtre_sonuc:
    print(k.acikadres)

filtre_sonuc = oturum.query(Ogrenci).filter(
    Ogrenci.email == "deneme@demene.com")
for k in filtre_sonuc:
    print(k.ad)

filtre_sonuc = oturum.query(Ogrenci).filter(Ogrenci.ad.like("H%"))
for a in filtre_sonuc:
    print(a.ad)

filtre_sonuc = oturum.query(Ogrenci).filter(Ogrenci.id.in_([1, 3, 5]))
for a in filtre_sonuc:
    print(str(a.id) + " "+a.ad)

fsonuc = oturum.query(Ogrenci).filter(
    and_(Ogrenci.ad.like("Ah%"), Ogrenci.id.in_([1, 5])))

for h in fsonuc:
    print(str(h.id) + " "+h.ad)

# or
fsonuc = oturum.query(Adres).filter(
    or_(Adres.acikadres.like("A%"), Adres.ogrenci_id.in_([1, 2, 3, 4])))
for h in fsonuc:
    print(str(h.id) + " "+h.acikadres)

# satir sayısı
satir_say = oturum.query(Ogrenci).count()
print(satir_say)


join_sonuc = oturum.query(Ogrenci, Adres).join(Adres)
for k in join_sonuc:
    print(k[0].ad + " "+k[1].acikadres)
