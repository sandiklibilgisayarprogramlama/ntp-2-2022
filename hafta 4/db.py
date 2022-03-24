from sqlite3 import connect
from adres import Adres


class AdresDB:
    def __init__(self, db_name):
        self.connection = connect(db_name)

    def tum_verileri_cek(self):
        query = "select * from Emlak"
        cur = self.connection.cursor()
        cur.execute(query)
        rows = cur.fetchall()
        emlak_listesi = []
        for ev in rows:
            emlak_listesi.append(Adres(ev[4], ev[1], ev[2], ev[3], ev[0]))

        return emlak_listesi

    def kirasi_en_yuksek_daireyi_yaz(self):
        adresler = self.tum_verileri_cek()
        kirasi_en_yuksek_adres = None
        yuksek_kira = 0
        for adres in adresler:
            if yuksek_kira < adres.kira:
                yuksek_kira = adres.kira
                kirasi_en_yuksek_adres = adres

        print(kirasi_en_yuksek_adres.adres)
        print(yuksek_kira)
