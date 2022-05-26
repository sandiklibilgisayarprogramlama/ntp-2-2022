"""
    kivy uygulamasını başlatan sınıftır.
"""
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.popup import Popup
from db import Kullanici, engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import and_

Session = sessionmaker(bind=engine)

oturum = Session()


class Uyari(Popup):
    """
        name :
        params : 
    """
    pass


class EkranYoneticisi(ScreenManager):
    """
        Ekranların değişmesi görevini gerçekleştir.
    """
    pass


class GuncelleSayfasi(Screen):
    def on_enter(self):
        global kisi_ad
        self.ids.kadiguncelle.text = kisi_ad

    def geri(self):
        self.parent.current = "kisisayfasi"

    def guncelle(self):
        yeni_alan = str(self.ids.kadiguncelle.text).strip()

        global kullanici_adi
        dbkullanici = oturum.query(Kullanici).filter(
            Kullanici.kullaniciadi == kullanici_adi).first()

        dbkullanici.ad = yeni_alan
        oturum.commit()
        global kisi_ad
        kisi_ad = yeni_alan
        self.parent.current = "kisisayfasi"


class KisiSayfasi(Screen):
    def on_enter(self):
        global kisi_ad
        self.ids.lblad.text = kisi_ad

    def geri(self):
        self.parent.current = "girissayfasi"

    def guncelle(self):
        self.parent.current = "guncellesayfasi"


class GirisSayfasi(Screen):

    def tikla(self):
        gelenkadi = str(self.ids.kadi.text).strip()
        gelensifre = str(self.ids.sifre.text).strip()
        gelenveri = oturum.query(Kullanici).filter(
            and_(Kullanici.kullaniciadi == gelenkadi,
                 Kullanici.sifre == gelensifre)).first()

        if (gelenveri):
            print("giriş başarılı")
            global kisi_ad
            kisi_ad = gelenveri.ad

            global kullanici_adi
            kullanici_adi = gelenveri.kullaniciadi

            self.parent.current = "kisisayfasi"
        else:
            print("giriş başarısız")
            popup = Uyari()
            popup.open()


class Main(App):
    def build(self):
        return EkranYoneticisi()


Main().run()
