from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.image import Image
#from quiz_final3 import QuizApp
from kivy.uix.label import Label
from kivy.core.window import Window
from kivy.config import Config
Window.clearcolor = (1, 0.9569, 0.7843, 1)
Config.set('graphics', 'resizable', False)
Window.size = (1200,700)
print("h3")
class Button(Button):
    def __init__(self, image_file, **kwargs):
        super().__init__(**kwargs)
        self.size_hint_x = None
        self.width = 500
        self.height = 90
        self.background_normal = image_file
        self.background_down = "brown.png"
        if "3.png" in image_file:
            self.bind(on_press=lambda instance: self.launch_quiz())

    def launch_quiz(self):
        # get the parent layout of the button
        outer_layout = self.parent.parent

        # remove all widgets from the parent layout
        for widget in outer_layout.children:
            outer_layout.remove_widget(widget)
        # get the root widget of the app
        root_widget = App.get_running_app().root

        # remove all widgets from the root widget
        for widget in root_widget.walk(restrict=True):
            root_widget.remove_widget(widget)
        
            

        # launch the QuizApp
        QuizApp().run()

            

class MainApp(App):
    
    def build(self):
        layout = BoxLayout(orientation='vertical', spacing=50, padding=[40, 300, 800, 40])
        for i in range(4):
            button = Button(image_file=f"{i + 1}.png", text='')
            layout.add_widget(button)

        outer_layout = FloatLayout(size=(800, 600))

        title_banner = Image(source='Carbon.png', size_hint=(None, None), size=(1950, 1420), pos=(500, 500))
        outer_layout.add_widget(title_banner)

        house = Image(source='house2.png', size_hint=(None, None), size=(1250, 1100), pos=(800, 20))
        

        outer_layout.add_widget(house)

        image = Image(source='Menu3.png', size_hint=(None, None), size=(550, 1350), pos=(20, 20))
        outer_layout.add_widget(image)

        outer_layout.add_widget(layout)
        
        return outer_layout

if __name__ == '__main__':
    MainApp().run()
