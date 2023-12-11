from kivy.lang import Builder
from kivy.properties import ObjectProperty
from kivymd.app import MDApp
from kivymd.uix.scrollview import MDScrollView
from kivy.core.window import Window
import random
from kivymd.uix.menu import MDDropdownMenu

# Adds content inside of the Navigation Drawer for the user to click on
class ContentNavigationDrawer(MDScrollView):
    screen_manager = ObjectProperty()
    nav_drawer = ObjectProperty()
# Class defining the main functionality of the app
class DND(MDApp):    
    def build(self):
        self.theme_cls.theme_style = 'Dark'
        self.theme_cls.primary_palette = 'Orange'
        Window.size = (350, 650)
        self.screen = Builder.load_file('DndApp.kv')
        # Menu_items provides a list of characters class that the character can choose from
        menu_items = [
            {
                "viewclass": "OneLineListItem",
                "text": "Artificer",
                "on_release": lambda x=f"Artificer": self.class_select(x)
            },
            {
                "viewclass": "OneLineListItem",
                "text": "Barbarian",
                "on_release": lambda x=f"Barbarian": self.class_select(x)
            },
            {
                "viewclass": "OneLineListItem",
                "text": "Bard",
                "on_release": lambda x=f"Bard": self.class_select(x)
            },
            {
                "viewclass": "OneLineListItem",
                "text": "Blood Hunter",
                "on_release": lambda x=f"Blood Hunter": self.class_select(x)
            },
            {
                "viewclass": "OneLineListItem",
                "text": "Cleric",
                "on_release": lambda x=f"Cleric": self.class_select(x)
            },
            {
                "viewclass": "OneLineListItem",
                "text": "Druid",
                "on_release": lambda x=f"Druid": self.class_select(x)
            },
            {
                "viewclass": "OneLineListItem",
                "text": "Fighter",
                "on_release": lambda x=f"Fighter": self.class_select(x)
            },
            {
                "viewclass": "OneLineListItem",
                "text": "Monk",
                "on_release": lambda x=f"Monk": self.class_select(x)
            },
            {
                "viewclass": "OneLineListItem",
                "text": "Paladin",
                "on_release": lambda x=f"Paladin": self.class_select(x)
            },
            {
                "viewclass": "OneLineListItem",
                "text": "Ranger",
                "on_release": lambda x=f"Ranger": self.class_select(x)
            },
            {
                "viewclass": "OneLineListItem",
                "text": "Rogue",
                "on_release": lambda x=f"Rogue": self.class_select(x)
            },
            {
                "viewclass": "OneLineListItem",
                "text": "Sorcerer",
                "on_release": lambda x=f"Sorcerer": self.class_select(x)
            },
            {
                "viewclass": "OneLineListItem",
                "text": "Warlock",
                "on_release": lambda x=f"Warlock": self.class_select(x)
            },
            {
                "viewclass": "OneLineListItem",
                "text": "Wizard",
                "on_release": lambda x=f"Wizard": self.class_select(x)
            } 
        ]
        self.menu = MDDropdownMenu(
            caller=self.screen.ids.class_id, # type: ignore
            items=menu_items,
            width_mult=3,
	    max_height= '200dp'
        )
        return self.screen

    # Updates class_name textfield when menu item is selected
    def class_select(self, text_item):
        self.root.ids.class_name.text = text_item # type: ignore
	self.menu.dismiss()	

     # Logic for the dice rolls for each dice if more than one
    def roll_dice(self):
        try:
            num_dice = int(self.root.ids.num_dice.text)# type: ignore
            num_sides = int(self.root.ids.num_sides.text)# type: ignore
            modifier = int(self.root.ids.modifier.text) if self.root.ids.modifier.text else 0 # type: ignore
            
            if num_dice <= 0:
                self.root.ids.result_output.text = "Invalid input"# type: ignore
                return
            
            rolls = [random.randint(1, num_sides) for dice in range(num_dice)]
            total = sum(rolls) + modifier
            result_text = f"Rolls: {rolls}\nTotal with modifier ({modifier}): {total}"
            self.root.ids.result_output.text = result_text# type: ignore

        except ValueError:
            self.root.ids.result_output.text = "Invalid input"# type: ignore

   # Button inputs for number of dice
    def on_press_dice(self, btn):
        self.root.ids.num_dice.text = btn.text# type: ignore
    def on_press_sides(self, btn):
        self.root.ids.num_sides.text = btn.text # type: ignore

    def reset_fields(self):
        self.root.ids.num_dice.text = "" # type: ignore
        self.root.ids.num_sides.text = "" # type: ignore
        self.root.ids.modifier.text = "" # type: ignore
        self.root.ids.result_output.text = "" # type: ignore

DND().run()
