class Adres:
    def __init__(self, metrekare, kira, cephe, adres, id=None):
        self.id = id
        self.metrekare = metrekare
        self.kira = kira
        self.cephe = cephe
        self.adres = adres

    def metre_kare_yazdir(self):
        print(self.metrekare)
