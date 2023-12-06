from kivymd.app import MDApp
from kivy.lang import Builder
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.menu import MDDropdownMenu

class Start(MDBoxLayout):
    def drpmenu(self,instance):
            self.menu_list = [
                { 
                    'viewclass': 'OneLineListItem',
                    'text': 'Example 1',
                    'on_release': lambda x : self.addbtn()
                }
            ]
            self.menu = MDDropdownMenu(items=self.menu_list,width_mult=2)
            self.menu.caller = instance
            self.menu.open()

    def addbtn(self):
        pass

class NewApp(MDApp):
    def build(self):
        Builder.load_file('new-app.kv')
        return Start()

        

NewApp().run()
