# coding=<UTF-8>
from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.core.window import Window


class CalculatorApp(MDApp):
    def build(self):
        # sets window size for the application and draws window to screen
        Window.size = (400,600)
        self.theme_cls.theme_style = 'Dark'
        self.theme_cls.primary_palette = 'Orange'
        return Builder.load_file('calculator.kv')
    
    # This function allows the user to input numbers and operators in the textbox
    def button_press(self, btn):
        if self.root.ids.num_input.text == '0':
            self.root.ids.num_input.text = '' + btn.text
        else:
            self.root.ids.num_input.text += btn.text

    #This function clears the textbox once the Del key is pressed
    def button_press_del(self, btn):
        if btn.text == 'Del':
            self.root.ids.num_input.text = '0'
    # This function takes two numbers from the textbox that is separated by an operator 
    # and evaluates them based on the operator being used 
    #    
    def solution(self):
        try:
            result = str(eval(self.root.ids.num_input.text)) # type: ignore
            self.root.ids.num_input.text = result # type: ignore
        # If the user does not complete the operation, the calculator will pull up an 
        # error message
        except Exception as e:
            self.root.ids.num_input.text = 'Error' # type: ignore
        
CalculatorApp().run()