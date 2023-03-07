import os
import glob

import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.graphics import Rectangle, Color
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.pagelayout import PageLayout
from kivy.uix.splitter import Splitter
from kivy.uix.screenmanager import ScreenManager, Screen
#
#
# class Mytest(Widget):
#     pass
#
#
# class MyApp(App):
#     def build(self):
#         return Mytest()
#
#
# if __name__ == '__main__':
#     MyApp().run()

dir = glob.glob("C:/Users/Vex-Advik's/Desktop/EnvCode/*".format('csv'))
print(dir)
