from kivy.lang import Builder
from kivy.properties import ObjectProperty
from kivymd.app import MDApp
from kivymd.uix.scrollview import MDScrollView
from kivy.core.window import Window
import random


class ContentNavigationDrawer(MDScrollView):
    screen_manager = ObjectProperty()
    nav_drawer = ObjectProperty()

class Example(MDApp):
    def build(self):
        Window.size = (350, 650)
        return Builder.load_file('new-app.kv')

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
    
    # Button inputs for changing the theme from light to dark
    def switch_theme(self):
        self.theme_cls.theme_style = 'Dark' if self.theme_cls.theme_style == 'Light' else 'Light'
    
   
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

Example().run()
