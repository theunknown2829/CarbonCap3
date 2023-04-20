from kivy.app import App
from kivy.config import Config
from kivy.core.window import Window
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
import random
import datetime
from kivy.uix.image import Image
from kivy.uix.floatlayout import FloatLayout


ADVICE_DICT = {
    'light': [
        "Unplug appliances \nwhen not in use.",
        "Turn off lights when \nleaving a room.",
        "Use energy-efficient \nlight bulbs.",
        "Install dimmer switches to \ncontrol the amount of light you use.",
        "Use natural light by opening \ncurtains or blinds during the day.",
        "Replace outdated fixtures with \nenergy-efficient ones.",
        "Use motion sensor lights \nto reduce energy waste.",
        "Choose lamps and\n lighting fixtures that \ndirect light where it's needed.",
        "Use task lighting \ninstead of \noverhead lighting.",
    ],
    'heat': [
        "Lower your thermostat\n in the winter and raise\n it in the summer.",
        "Install a programmable \nthermostat.",
        "Seal air leaks around \nwindows and doors.",
        "Use a space heater\n instead of heating an entire room.",
        "Insulate your home \nto prevent heat loss.",
        "Close curtains\n or blinds at night\n to keep heat in.",
        "Wear warmer \nclothes instead of cranking\n up the heat.",
        "Use draft stoppers\n to prevent cold air\n from coming in.",
        "Use a humidifier to\n add moisture to the air, \nwhich can make it feel warmer.",
    ],
    'appliances': [
        "Use a clothesline\n instead of a dryer.",
        "Wash full loads of\n laundry and dishes.",
        "Choose energy-efficient \nappliances.",
        "Use a microwave or \ntoaster oven instead\n of a regular oven.",
        "Defrost food in \nthe refrigerator instead \nof using a microwave.",
        "Clean your appliances \nregularly to ensure they are \nworking efficiently.",
        "Use a slow cooker\n instead of the oven to \ncook meals.",
        "Opt for a laptop\n instead of a desktop computer, as they\n use less energy.",
        "Unplug electronics\n when not in use to reduce \nstandby power usage.",
    ],
    'water': [
        "Take shorter\n showers.",
        "Use a low-flow \nshowerhead.",
        "Fix any leaks.",
        "Use a dishwasher \ninstead of washing\n dishes by hand.",
        "Scrape dishes \ninstead of rinsing\n them before putting\n them in the dishwasher.",
        "Collect and reuse\n greywater from your shower\n or washing machine for\n watering plants.",
        "Use a broom instead of\n a hose to clean \noutdoor spaces.",
        "Turn off the tap\n when brushing your \nteeth or shaving.",
        "Use a bucket to \ncollect and reuse water for\n plants instead of using a hose.",
    ],
}

GREETINGS = ['Hi!', 'Hello!', 'Hey there!', 'Greetings!']
FOLLOW_UP = ['What else can I help you with?', 'Is there anything else you would \n like to know?', 'Do you have any other questions?']

class EnergySaverApp(App):
    def build(self):
        # Create a FloatLayout for the root widget
        root = FloatLayout()
        
        # Add the background image to the root widget
        image1 = Image(source='images/chatbot2.png')

        # Add the label widget to the root widget and position it on top of the image
        self.advice_label = Label(text="Hi, I'm Energía, your virtual assistant!\n How can I help you save energy today?\n Water, Lighting,Heating or Appliances?", font_size=55, font_name='Roboto', halign='center', color=(0, 0, 0, 1), size_hint=(1, None), height=500)
        self.advice_label.pos_hint = {'center_x': 0.66, 'center_y': 0.5} # adjust position as needed
        # Add the remaining widgets to the root widget
        self.category_input = TextInput(text="", multiline=False, font_size=24, halign='left', size_hint=(1, 0.1), height=40, background_color=(0.713, 0.576, 0.435, 1.0))
        self.category_input.bind(on_text_validate=self.get_advice)
        self.help_label = Label(text='', halign='right', color=(0, 0, 0, 1), font_size=55, font_name='Roboto', size_hint=(1, None), height=500)
        self.help_label.pos_hint = {'center_x': 0.66, 'center_y': 0.4} # adjust position as needed
        home_button = Image(source='images/home.png', size_hint=(0.15, 0.15), size=(100, 50))
        home_button.pos_hint = {'center_x': 0.93, 'y': 0.14}
        home_button.bind(on_touch_down=self.home)
        root.add_widget(self.category_input)
        root.add_widget(image1)
        root.add_widget(self.help_label)
        root.add_widget(self.advice_label)
        root.add_widget(home_button)
        
        # Return the root widget
        return root


    def home(self, instance, touch):
        from HOMEPAGE_40 import MainApp
        if instance.collide_point(*touch.pos):
            root_widget = App.get_running_app().root
            for widget in root_widget.walk(restrict=True):
                root_widget.remove_widget(widget)
            main_app = MainApp()
            main_app.run()



    TERM_TO_CATEGORY = {
        'lighting': [
            'light',
            'bulbs'],
        'heating': ['heat',],
        'appliances': ['appliances',],
        'water': ['water',]
    }

    def get_advice(self, *args):
        user_input = self.category_input.text.lower()
        if any(greeting in user_input for greeting in ['hi', 'hello', 'hey']):
            self.advice_label.text = random.choice(GREETINGS)
        elif any(greeting in user_input for greeting in ['bye', 'goodbye']):
            self.advice_label.text = "Goodbye!"
            self.category_input.disabled = True
        else:
            category = next((category for category in ADVICE_DICT if category in user_input), None)
            if not category:
                for term, term_category in self.TERM_TO_CATEGORY.items():
                    if term in user_input:
                        category = ADVICE_DICT.get(term_category)
                        break
            if category:
                advice = random.choice(ADVICE_DICT[category])
                self.advice_label.text = f"{category.capitalize()} tip: {advice}"
            else:
                self.advice_label.text = "Sorry, I didn't understand. Please try again."
        self.help_label.text = random.choice(FOLLOW_UP)
        self.category_input.text = ''
    

if __name__ == '__main__':
    Config.set('graphics', 'resizable', False)
    Window.size = (1200, 700)
    Window.clearcolor = (1, 0.9569, 0.7843, 1)
    EnergySaverApp().run()
