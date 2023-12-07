from kivy.lang import Builder
from kivy.properties import ObjectProperty
from kivymd.app import MDApp
from kivymd.uix.scrollview import MDScrollView
from kivy.core.window import Window


class ContentNavigationDrawer(MDScrollView):
    screen_manager = ObjectProperty()
    nav_drawer = ObjectProperty()

class Example(MDApp):
    def build(self):
        Window.size = (350, 650)
        return Builder.load_file('new-app.kv')


Example().run()