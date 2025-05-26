from kivy.app import App
from kivy.lang import Builder
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.label import Label
from kivy.uix.image import Image



class MyAppApp(App):
    def build(self):
        return Builder.load_file('MyApp.kv')


if __name__ == '__main__':
    MyAppApp().run()