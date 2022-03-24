

"""sqlalchemy -> 

pip install sqlalchemy
pip3 install sqlalchemy
python -m pip install sqlachemy
py -m pip install sqlachemy


orm -> object related mapping

kullanıcı Sınıfı
ad,soyad,yas

db
kullanici
id,ad,soyad,yas
select * from kullanici
for row in rows:
    id=row[0]
    ad = row[1]
"""


# insert into
from db import students, addresses, engine

# insert into students (ad,soyad,yas) values("ahmet","uzun",12)

eklenecek_ogrenci = students.insert().values(ad="ahmet", soyad="uzun", yas=12)
baglanti = engine.connect()
# baglanti.execute(eklenecek_ogrenci)


gelen_ogrenci = students.select()  # select * from ogrenci
sonuc = baglanti.execute(gelen_ogrenci)
sonuc_liste = sonuc.all()
for row in sonuc_liste:
    print(row.ad)

# benzer şekilde adres tablosuna kayıt ekleyiniz.
# daha sonra update ve delete işlemini yapmaya çalışınız.
