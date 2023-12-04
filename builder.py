builder = """
MDBoxLayout:
    orientation: 'vertical'
    
    MDTopAppBar:
        title: ""
        right_action_items: [['lightbulb-on-outline', lambda x: app.switch_theme_Light(), 'Theme: Light/Dark']]
        md_bg_color: app.theme_cls.bg_normal
        specific_text_color: 'gray'
        elevation: 0

    MDScreen:

        MDTextField:
            id: num_dice
            hint_text: "Number of Dice"
            input_filter: "int"
            pos_hint: {'center_x': .5, 'center_y': .9}
            size_hint_x: .9 
            width: 300
            hint_text_color_normal: 'gray'
            line_color_normal: 'gray'
            text_color_normal: 'gray'

        MDRaisedButton:
            text: "1"
            on_release: app.on_press_dice(self)
            pos_hint: {'center_x': .12, 'center_y': .8}
            

        MDRaisedButton:
            text: "2"
            on_release: app.on_press_dice(self)
            pos_hint: {'center_x': .31, 'center_y': .8}
            
        MDRaisedButton:
            text: "3"
            on_release: app.on_press_dice(self)
            pos_hint: {'center_x': .5, 'center_y': .8}
            
        MDRaisedButton:
            text: "4"
            on_release: app.on_press_dice(self)
            pos_hint: {'center_x': .69, 'center_y': .8}

        MDRaisedButton:
            text: "5"
            on_release: app.on_press_dice(self)
            pos_hint: {'center_x': .88, 'center_y': .8}

        MDRaisedButton:
            text: "6"
            on_release: app.on_press_dice(self)
            pos_hint: {'center_x': .12, 'center_y': .7}

        MDRaisedButton:
            text: "7"
            on_release: app.on_press_dice(self)
            pos_hint: {'center_x': .31, 'center_y': .7}

        MDRaisedButton:
            text: "8"
            on_release: app.on_press_dice(self)
            pos_hint: {'center_x': .5, 'center_y': .7}

        MDRaisedButton:
            text: "9"
            on_release: app.on_press_dice(self)
            pos_hint: {'center_x': .69, 'center_y': .7}

        MDRaisedButton:
            text: "10"
            on_release: app.on_press_dice(self)
            pos_hint: {'center_x': .88, 'center_y': .7}


        MDTextField:
            id: num_sides
            hint_text: "Number of Sides"
            input_filter: "int"
            pos_hint: {'center_x': .5, 'center_y': .6}
            size_hint_x: .9 
            width: 300
            hint_text_color_normal: 'gray'
            line_color_normal: 'gray'
            text_color_normal: 'gray'

        MDRaisedButton:
            text: "20"
            on_release: app.on_press_sides(self)
            pos_hint: {'center_x': .3, 'center_y': .5}

        MDRaisedButton:
            text: "12"
            on_release: app.on_press_sides(self)
            pos_hint: {'center_x': .5, 'center_y': .5}

        MDRaisedButton:
            text: "10"
            on_release: app.on_press_sides(self)
            pos_hint: {'center_x': .7, 'center_y': .5}

        MDRaisedButton:
            text: "8"
            on_release: app.on_press_sides(self)
            pos_hint: {'center_x': .3, 'center_y': .4}

        MDRaisedButton:
            text: "6"
            on_release: app.on_press_sides(self)
            pos_hint: {'center_x': .5, 'center_y': .4}
        
        MDRaisedButton:
            text: "4"
            on_release: app.on_press_sides(self)
            pos_hint: {'center_x': .7, 'center_y': .4}

        MDTextField:
            id: modifier
            hint_text: "Modifier"
            input_filter: "int"
            pos_hint: {'center_x': .5, 'center_y': .3}
            size_hint_x: .9
            width: 400
            hint_text_color_normal: 'gray'
            line_color_normal: 'gray'
            text_color_normal: 'gray'
        

        MDTextField:
            id: result_output
            hint_text: "Result"
            readonly: True
            pos_hint: {'center_x': .5, 'center_y': .2}
            size_hint_x: .9
            width: 800
            hint_text_color_normal: 'gray'
            line_color_normal: 'gray'
            text_color_normal: 'gray'

        MDRaisedButton:
            text: "Roll Dice"
            on_release: app.roll_dice()
            pos_hint: {'center_x': .35, 'center_y': .1}
            size_hint_x: None
            width: 300

        MDRaisedButton:
            text: "Reset Dice"
            on_release: app.reset_fields()
            pos_hint: {'center_x': .65, 'center_y': .1}
            size_hint_x: None 
            width: 300
            
"""