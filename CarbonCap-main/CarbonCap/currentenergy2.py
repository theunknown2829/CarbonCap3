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
        fig, ax = plt.subplots(figsize=(15,15))
        home_button = Button(background_normal='images/home.png', size_hint=(None, None), size=(200, 200), pos_hint={'right': 0.95, 'y': 0.05})
        home_button.bind(on_press=self.go_home)
        fig.set_facecolor("#FFF3C8")
        ax.set_facecolor("#FFF3C8")
        layout = BoxLayout(orientation='vertical')
        energy_distribution = [30, 20, 10, 15, 5, 20]
        labels = ['Refrigerator', 'Washing Machine', 'Air Conditioner', 'Lighting', 'Television', 'Other']
        wedges, texts, autotexts = plt.pie(energy_distribution, labels=labels, autopct='%1.1f%%',)
        plt.setp(autotexts, size=20)
        plt.title('Energy Distribution Across Household', size=30)
        plt.legend(wedges, labels, loc="best")
        plt.savefig('pie_chart.png')
        image = Image(source='pie_chart.png', allow_stretch=True, keep_ratio=True,size_hint=(0.5, 0.5))
        total_label = Label(text=f'Total Energy Used: 95 kW', size_hint=(1, None), height=80 , color='black',bold=True,font_size=60)
        layout.add_widget(total_label)
        layout.add_widget(image)
        layout.add_widget(home_button)
        return layout

    def go_home(self, instance):
        # Implement this method to go back to the home screen when the home button is pressed
        pass

Energy().run()
