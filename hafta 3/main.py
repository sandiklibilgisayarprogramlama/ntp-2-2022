from adresdb import AdresDB
from kullanici import Kullanici
from kullanicidb import KullaniciDB
from database import DB

db = KullaniciDB("deneme.db")
db.veri_ekle("kullanici", Kullanici(100, "ahmet", "uzun", 12))
kullanici_list = db.tum_verileri_getir("kullanici")

for kullanici in kullanici_list:
    kullanici.adiEkranaYaz()

adres_db = AdresDB("deneme.db")
adresler = adres_db.tum_verileri_getir("adres")

for adres in adresler:
    print(adres.mahalle)
