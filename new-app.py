from kivymd.app import MDApp
from kivy.lang import Builder

class NewApp(MDApp):
    def build(self):
        self.title = "Idk what this app is supposed to be right now"
        return Builder.load_file('new-app.kv')

NewApp().run()