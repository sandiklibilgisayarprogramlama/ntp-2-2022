from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.window import Window
Window.size = (400, 700)


class EkranYoneticisi(ScreenManager):
    """
        Ekranların değişmesi görevini gerçekleştir.
    """
    pass


class HesapMakinesi(Screen):

    def add(self, number):
        self.ids.lblinp2.text = self.ids.lblinp2.text+number

    def c_click(self):
        self.ids.lblinp1.text = "0"
        self.ids.lblinp2.text = ""

    def left_bracket_click(self):
        self.add("(")

    def right_bracket_click(self):
        self.add(")")

    def divide_click(self):
        self.add("/")

    def seven_click(self):
        self.add("7")

    def eight_click(self):
        self.add("8")

    def nine_click(self):
        self.add("9")

    def multiply_click(self):
        self.add("*")

    def four_click(self):
        self.add("4")

    def five_click(self):
        self.add("5")

    def six_click(self):
        self.add("6")

    def minus_click(self):
        self.add("-")

    def one_click(self):
        self.add("1")

    def two_click(self):
        self.add("2")

    def three_click(self):
        self.add("3")

    def plus_click(self):
        self.add("+")

    def zero_click(self):
        self.add("0")

    def dot_click(self):
        self.add(".")

    def equals_click(self):
        try:
            self.ids.lblinp1.text = str(eval(self.ids.lblinp2.text))
        except:
            self.ids.lblinp1.text = "Error"

    def empty_click(self):
        pass


class Main(App):
    def build(self):
        return EkranYoneticisi()


Main().run()
