#!/usr/bin/env python
import os

from kivy.config import Config
Config.set('graphics', 'resizable', True)
Config.set('graphics', 'minimum_width', 700)
Config.set('graphics', 'minimum_height', 500)
from kivy.app import App
os.environ['KIVY_IMAGE'] = 'pil,sdl2'
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder
from TabbedPanel.MyTabbedPanel import MyTabbedPanel
from kivy.uix.tabbedpanel import TabbedPanelHeader
from Layouts.MyGridLayout import MyGridLayout
from kivy.factory import Factory

Builder.load_file('Layouts/layout.kv')


class HomeScreen(Screen):
    pass


class SecondScreen(Screen):
    pass


class HelpScreen(Screen):
    pass


class SplashScreen(Screen):
    pass


class ClosingHeader(TabbedPanelHeader):
    pass


Factory.register('ClosingHeader', cls=ClosingHeader)


# Custom TabbedPanelItem
class MyTabbedPanelItem(MyTabbedPanel):

    # Add closing header
    def add_header(self, content):
        self.add_widget(ClosingHeader(panel=self, content=content))


class RootScreen(ScreenManager):
    pass


class MAB(App):
    icon = 'res/slot_img.png'

    def build(self):
        return RootScreen()


if __name__ == "__main__":
    MAB().run()
