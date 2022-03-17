from database import DB
from kullanici import Kullanici


class KullaniciDB(DB):
    def __init__(self, db_name):
        super().__init__(db_name)

    def tum_verileri_getir(self, table_name):
        kullanici_list = []
        rows = super().tum_verileri_getir(table_name)
        for row in rows:
            print(row)
            kull = Kullanici(row[0], row[1], row[2], row[3])
            kullanici_list.append(kull)
        return kullanici_list
