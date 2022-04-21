class Urun:
    def __init__(self, ad, ucret):
        self.ad = ad
        self.ucret = ucret


class Kisi:
    def __init__(self, ad, para, alinan_listesi):
        self.ad = ad
        self.para = para
        self.alinan_listesi = alinan_listesi

    def kalan_para_ekrana_yazdir(self):
        verilecek_ucret = 0
        for alinan in self.alinan_listesi:
            verilecek_ucret = verilecek_ucret + alinan.ucret

        print(self.para-verilecek_ucret)


meyve = Urun("meyve", 10)
sebze = Urun("sebze", 20)

burcu = Kisi("burcu", 60, [meyve, sebze])
burcu.kalan_para_ekrana_yazdir()
