class Kullanici:
    def __init__(self, id, ad, soyad, yas):
        self.id = id
        self.ad = ad
        self.soyad = soyad
        self.yas = yas

    def adiEkranaYaz(self):
        print(self.ad)

    def send_data(self):
        return (self.ad, self.soyad, self.yas)
