from kivy.app import App
from kivy.lang import Builder

GUI = Builder.load_file('gui.kv')

class MeuAplicativo(App):
    def build(self):
        return GUI

MeuAplicativo().run()