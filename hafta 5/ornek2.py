from numpy import ogrid
from soupsieve import select
from db import engine, addresses


baglanti = engine.connect()
"""
sql_kod = addresses.insert().values(ogrenci_id=1, acikadres="afyon")
print(sql_kod)
baglanti.execute(sql_kod)
"""
select_kod = addresses.select()
sonuc = baglanti.execute(select_kod)
print(sonuc.fetchall())

# update
update_kod = addresses.update().where(
    addresses.c.ogrenci_id == 1).values(acikadres="ısparta")
sonuc = baglanti.execute(update_kod)
print(sonuc)

# delete
delete_kod = addresses.delete().where(addresses.c.ogrenci_id == 1)
baglanti.execute(delete_kod)


# kullanıcı adlı veritabanında kullanıcı adı, şifre ve ad bilgisi tutulmaktadır.
# buna göre konsoldan girilen kullanıcı adı ve şifre bilgileri doğruyla
# ekrana hoşgeldin ad, yanlışsa ise bilgilerinizden biri yanlış yazan
# programı kodlayınız.
