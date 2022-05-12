from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen

from db import Kullanici, engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import and_

Session = sessionmaker(bind=engine)

oturum = Session()


class EkranYoneticisi(ScreenManager):
    pass


class KisiSayfasi(Screen):
    pass


class GirisSayfasi(Screen):

    def tikla(self):
        gelenkadi = str(self.ids.kadi.text).strip()
        gelensifre = str(self.ids.sifre.text).strip()
        gelenveri = oturum.query(Kullanici).filter(
            and_(Kullanici.kullaniciadi == gelenkadi,
                 Kullanici.sifre == gelensifre)).first()

        if (gelenveri):
            print("giriş başarılı")
            print(gelenveri.ad)
            self.parent.current = "kisisayfasi"
        else:
            print("giriş başarısız")


class Main(App):
    def build(self):
        return EkranYoneticisi()


Main().run()
