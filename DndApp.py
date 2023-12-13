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
        items = [
            'Artificer', 'Barbarian', 'Bard', 'Blood Hunter', 'Cleric', 'Druid', 'Fighter',
            'Monk', 'Paladin', 'Ranger', 'Rogue', 'Sorcerer', 'Warlock', 'Wizard', 
        ]
        menu_items = [
            {
                "viewclass": "OneLineListItem",
                "text": f"{item}",
                "on_release": lambda x=f"{item}": self.class_select(x)
            } for item in items 
        ]
        level_items = [
            {
                "viewclass": "OneLineListItem",
                "text": f"{i}",
                "on_release": lambda x=f"{i}": self.level_select(x)
            } for i in range(1, 20+1)
        ]
        self.menu = MDDropdownMenu(
            caller=self.screen.ids.class_id, # type: ignore
            items=menu_items,
            width_mult=3,
            max_height= '300dp'
        )
        self.level = MDDropdownMenu(
            caller=self.screen.ids.level_id, # type: ignore
            items=level_items,
            width_mult=3,
            max_height= '300dp'
        )
        return self.screen


    # Updates class button and level button text when menu item is selected
    def class_select(self, text_item):
        self.root.ids.class_id.text = text_item # type: ignore
        self.menu.dismiss()
    def level_select(self, text_item):
        self.root.ids.level_id.text = "LEVEL" + " " + text_item # type: ignore
        self.level.dismiss()

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
