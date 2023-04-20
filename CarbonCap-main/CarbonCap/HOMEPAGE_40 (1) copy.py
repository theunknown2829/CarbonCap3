from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.image import Image
from kivy.uix.label import Label
from kivy.core.window import Window
from kivy.config import Config
from kivy.uix.widget import Widget
from kivy.graphics import Rectangle
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from quiz_final4 import QuizApp
from AdviceApp import EnergySaverApp
from kivy.lang import Builder
from PredictionApp import preds
from Controls import control


class MainApp(App):
    def build(self):
        class MyScreen(Screen):
            def launch_quiz(self):
                sm = App.get_running_app().root
                sm.switch_to(QuizScreen())

            def launch_advice(self):
                sm = App.get_running_app().root
                sm.switch_to(AdviceScreen())

            def launch_prediction(self):
                sm = App.get_running_app().root
                sm.switch_to(PredictionScreen())

            def launch_controls(self):
                sm = App.get_running_app().root
                sm.switch_to(ControlsScreen())

        class QuizScreen(Screen):
            def on_enter(self):
                App.get_running_app().stop()
                QuizApp().run()

        class AdviceScreen(Screen):
            def on_enter(self):
                App.get_running_app().stop()
                EnergySaverApp().run()


        class PredictionScreen(Screen):
            def on_enter(self):
                App.get_running_app().stop()
                from PredictionApp import preds
                print(0)
                return preds()
            
                
        class ControlsScreen(Screen):
            def on_enter(self):
                App.get_running_app().stop()
                control().run()

        class WindowManager(ScreenManager):
            pass

        Builder.load_file('my.kv')
        sm = WindowManager()

        sm.add_widget(MyScreen(name='main'))
        sm.add_widget(QuizScreen(name='quiz'))
        sm.add_widget(AdviceScreen(name='advice'))
        sm.add_widget(PredictionScreen(name='prediction'))
        sm.add_widget(ControlsScreen(name='controls'))

        Window.clearcolor = (1, 0.9569, 0.7843, 1)
        Config.set('graphics', 'resizable', False)  
        return sm



if __name__ == '__main__':
    MainApp().run()


