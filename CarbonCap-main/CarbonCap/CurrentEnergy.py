import matplotlib.pyplot as plt
from kivy.app import App
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.graphics import Rectangle, Color
from kivy.uix.label import Label
from kivy.core.window import Window
from kivy.uix.image import Image
from kivy.uix.scatter import Scatter
from kivy.config import Config
Config.set('graphics', 'resizable', False)
Window.clearcolor = (1, 0.9569, 0.7843, 1)
class Energy(App):

    def build(self):
        fig, ax = plt.subplots(figsize=(10,7))
        fig.set_facecolor("#FFF3C8")
        ax.set_facecolor("#FFF3C8")
        layout = BoxLayout(orientation='vertical')
        energy_distribution = [30, 20, 10, 15, 5, 20]
        labels = ['Refrigerator', 'Washing Machine', 'Heating', 'Lighting', 'Television', 'Other']
        plt.pie(energy_distribution, labels=labels)
        layout.canvas.before.clear()
        layout.canvas.before.add(Color(1, 0.95, 0.78, 1))
        layout.canvas.before.add(Rectangle(pos=layout.pos, size=layout.size))
        plt.title('Energy Distribution Across Household', size=20)
        plt.savefig('pie_chart.png')
        image = Image(source='pie_chart.png', allow_stretch=True, keep_ratio=False)
        total_label = Label(text=f'Total Energy Used: 95 kW', size_hint=(1, None), height=80 , color='black',bold=True,font_size=60)
        layout.add_widget(total_label)
        layout.add_widget(image)
        home_button = Button(background_normal='images/home.png', size_hint=(None, None), size=(220, 220), pos_hint={'right': 0.95, 'y': 0.05})
        home_button.bind(on_press=self.go_home)
        layout.add_widget(home_button)

        return layout
    def go_home(self, instance):
        from HOMEPAGE_40 import MainApp
        #if instance.collide_point(*touch.pos):
        root_widget = App.get_running_app().root
        for widget in root_widget.walk(restrict=True):
            root_widget.remove_widget(widget)
        main_app = MainApp()
        main_app.run()


Energy().run()
