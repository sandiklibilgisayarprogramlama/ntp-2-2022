from kivy.app import App


class Main(App):
    # ilk build
    def on_start(self):
        self.title = "Yazbel"
        # bir takım işlemler...

    def on_stop(self):
        # Uygulama kapatılırken...
        pass

    def on_pause(self):
        # Uygulama arkaplana alınırken...
        # Burda return True yapmanız gerekiyor
        return True

    def on_resume(self):
        # Tekrar giriş yapıldığında yazımızı değiştiriyoruz
        self.title = "Programa tekrar hoşgeldiniz"


program = Main()
program.run()
