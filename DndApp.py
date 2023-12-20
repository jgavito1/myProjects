from kivy.lang import Builder
from kivy.properties import ObjectProperty
from kivymd.app import MDApp
from kivymd.uix.scrollview import MDScrollView
import random
from kivymd.uix.menu import MDDropdownMenu
from menu_items import class_item, race, all_subraces, alignments


# Adds content inside of the Navigation Drawer for the user to click on
class ContentNavigationDrawer(MDScrollView):
    screen_manager = ObjectProperty()
    nav_drawer = ObjectProperty()
# Class defining the main functionality of the app
class DND(MDApp):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.screen = Builder.load_file('DndApp.kv')
        menu_items = [
            {
                "viewclass": "OneLineListItem",
                "text": f"{item}",
                "on_release": lambda x=f"{item}": self.class_select(x)
            } for item in class_item 
        ]
        self.menu = MDDropdownMenu(
            caller=self.screen.ids.class_id, # type: ignore
            items=menu_items,
            width_mult=3,
            max_height= '300dp'
        )
        level_items = [
            {
                "viewclass": "OneLineListItem",
                "text": f"{i}",
                "on_release": lambda x=f"{i}": self.level_select(x)
            } for i in range(1, 20+1)
        ]
        self.level = MDDropdownMenu(
            caller=self.screen.ids.level_id, # type: ignore
            items=level_items,
            width_mult=3,
            max_height= '300dp'
        )
        race_items = [
            {
                "viewclass": "OneLineListItem",
                "text": f"{item}",
                "on_release": lambda x=f"{item}": self.race_select(x)
            } for item in race
        ]
        self.race = MDDropdownMenu(
            caller=self.screen.ids.race_id, # type: ignore
            items=race_items,
            width_mult=3,
            max_height= '300dp'
        )
        subrace_items = [
            {
                "viewclass": "OneLineListItem",
                "text": f"{item}",
                "on_release": lambda x=f"{item}": self.subrace_select(x)
            } for item in all_subraces
        ]
        self.subrace = MDDropdownMenu(
            caller=self.screen.ids.subrace_id, # type: ignore
            items=subrace_items,
            width_mult=3,
            max_height= '300dp'
        )
        alignment_items = [
            {
                "viewclass": "OneLineListItem",
                "text": f"{item}",
                "on_release": lambda x=f"{item}": self.alignment_select(x)
            } for item in alignments
        ]
        self.alignment = MDDropdownMenu(
            caller=self.screen.ids.subrace_id, # type: ignore
            items=alignment_items,
            width_mult=3,
            max_height= '300dp'
        )
    # Updates class, level, race, and subrace buttons on press
    def class_select(self, text_item):
        self.root.ids.class_id.text = text_item # type: ignore
        self.menu.dismiss()
    def level_select(self, text_item):
        self.root.ids.level_id.text = "LEVEL" + " " + text_item # type: ignore
        self.level.dismiss()
    def race_select(self, text_item):
        self.root.ids.race_id.text = text_item # type: ignore
        self.race.dismiss()
    def alignment_select(self, text_item):
        self.root.ids.alignment_id.text = text_item  # type: ignore
        self.alignment.dismiss()
    def subrace_select(self, text_item):
        if self.root.ids.race_id.text == 'DWARF': # type: ignore
            if text_item == 'HILL DWARF':
                self.root.ids.subrace_id.text = 'HILL DWARF' # type: ignore
            elif text_item == 'MOUNTAIN DWARF':
                self.root.ids.subrace_id.text = 'MOUNTAIN DWARF' # type: ignore
            else:
                self.root.ids.subrace_id.text = 'NOT A VALID SUBRACE' # type: ignore
        elif self.root.ids.race_id.text == 'ELF': # type: ignore
            if text_item == 'HIGH ELF':
                self.root.ids.subrace_id.text = 'HIGH ELF' # type: ignore
            elif text_item == 'WOOD ELF':
                self.root.ids.subrace_id.text = 'WOOD ELF' # type: ignore
            elif text_item == 'DARK ELF':
                self.root.ids.subrace_id.text = 'DARK ELF' # type: ignore
            else:
                self.root.ids.subrace_id.text = 'NOT A VALID SUBRACE' # type: ignore
        elif self.root.ids.race_id.text == 'HALFLING': # type: ignore
            if text_item == 'LIGHTFOOT HALFLING':
                self.root.ids.subrace_id.text = 'LIGHTFOOT HALFLING' # type: ignore
            elif text_item == 'STOUT HALFLING':
                self.root.ids.subrace_id.text = 'STOUT HALFLING' # type: ignore
            else:
                self.root.ids.subrace_id.text = 'NOT A VALID SUBRACE' # type: ignore
        elif self.root.ids.race_id.text == 'GNOME': # type: ignore
            if text_item == 'FOREST GNOME':
                self.root.ids.subrace_id.text = 'FOREST GNOME' # type: ignore
            elif text_item == 'ROCK GNOME':
                self.root.ids.subrace_id.text = 'ROCK GNOME' # type: ignore
            else:
                self.root.ids.subrace_id.text = 'NOT A VALID SUBRACE' # type: ignore
        else:
            self.root.ids.subrace_id.text = f'NO {self.root.ids.race_id.text} SUBRACES' # type: ignore
        self.subrace.dismiss()
    
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

    def build(self):
        self.theme_cls.theme_style = 'Dark'
        return self.screen
    
DND().run()
