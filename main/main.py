from kivymd.app import MDApp
from kivy.core.window import Window

class Kriv(MDApp):
    def build(self):
        Window.size = (300, 600)
        return


Kriv().run()
