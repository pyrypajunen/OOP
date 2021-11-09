from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen


class ScreenOne(Screen):
    
    def search_img(self):
        pass

class RootWidgets(ScreenManager):
    """Create the manager"""
    pass
    
class MainApp(App):
    """This class is a child class from the kivy App class."""
    
    def build(self):
        return RootWidgets()
    

MainApp().run()