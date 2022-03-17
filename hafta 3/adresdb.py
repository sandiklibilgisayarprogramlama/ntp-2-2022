from database import DB
from adres import Adres


class AdresDB(DB):
    def __init__(self, db_name):
        super().__init__(db_name)

    def tum_verileri_getir(self, table_name):
        _list = []
        rows = super().tum_verileri_getir(table_name)
        for row in rows:
            print(row)
            kull = Adres(row[0], row[1], row[2], row[3], row[4])
            _list.append(kull)
        return _list
