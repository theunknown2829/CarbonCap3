from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.config import Config
from kivy.utils import get_color_from_hex
from kivy.core.window import Window


Config.set('graphics', 'width', '800')
Config.set('graphics', 'height', '600')
Window.clearcolor = get_color_from_hex('#FFFFFF')


class EnergyWindow(BoxLayout):
    def __init__(self, **kwargs):
        super(EnergyWindow, self).__init__(**kwargs)

        self.current_temp = TextInput()
        self.prediction_month = TextInput()

        # set up the layout
        layout = GridLayout(cols=2, spacing=10, padding=50, size_hint=(None, None), size=(500, 300), pos_hint={'center_x': 0.4, 'center_y': 0.5})
        self.add_widget(layout)

        # add the input fields and labels
        layout.add_widget(Label(text="Current temperature:", size_hint_x=None, width=400, font_size=60, color=(0, 0, 0, 1)))
        layout.add_widget(self.current_temp)
        layout.add_widget(Label(text="Prediction month:", size_hint_x=None, width=400, font_size=60, color=(0, 0, 0, 1)))
        layout.add_widget(self.prediction_month)

        # add the predict button
        predict_button = Button(text="Predict", size_hint_x=None, width=200, height=50)
        predict_button.bind(on_release=self.predict)
        layout.add_widget(predict_button)

    def predict(self, *args):
        current_temp = float(self.current_temp.text)
        prediction_month = self.prediction_month.text
        # code for prediction goes here
        print(f"Predicting for temperature {current_temp} in month {prediction_month}...")


class EnergyApp(App):
    def build(self):
        return EnergyWindow()


if __name__ == '__main__':
    EnergyApp().run()
