from kivymd.app import MDApp
from kivy.lang import Builder
import random
from kivy.core.window import Window
from builder import builder



class DiceRollerV2App(MDApp):
    # Sets the window size to the approximate size of a Galaxy S20+
    Window.size = (350, 650)

    # Builds the application using a builder
    def build(self):
        self.theme_cls.theme_style = 'Dark'
        self.theme_cls.primary_palette = 'Orange'
        self.title = 'D&D Dice Roller'      
        return Builder.load_string(builder)

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
    def switch_theme_Light(self):
        self.theme_cls.theme_style = 'Light' if self.theme_cls.theme_style == 'Dark' else 'Dark'
    
   
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


DiceRollerV2App().run()
