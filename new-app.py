from kivy.lang import Builder
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.app import MDApp



class ContentNavigationDrawer(MDBoxLayout):
    pass

class NewApp(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Light"
        return Builder.load_file('new-app.kv')


NewApp().run()
