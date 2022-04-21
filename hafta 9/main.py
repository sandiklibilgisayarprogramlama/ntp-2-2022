from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from db import Kullanici, engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import and_

Session = sessionmaker(bind=engine)

oturum = Session()


class MainLayout(BoxLayout):
    def tikla(self):
        gelenkadi = str(self.ids.kadi.text).strip()
        gelensifre = str(self.ids.sifre.text).strip()
        gelenveri = oturum.query(Kullanici).filter(
            and_(Kullanici.kullaniciadi == gelenkadi,
                 Kullanici.sifre == gelensifre)).first()

        if (gelenveri):
            print("giriş başarılı")
            print(gelenveri.ad)
        else:
            print("giriş başarısız")


class Main(App):
    def build(self):
        return MainLayout()


Main().run()
