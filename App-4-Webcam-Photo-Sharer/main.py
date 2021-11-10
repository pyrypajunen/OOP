### IMPORTS ###
import wikipedia
import requests
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder
import time

# Loading frontend file
Builder.load_file('frontend.kv')

class ScreenOne(Screen):
    """Creating dynamic wikipedia image changer method"""
    
    def search_img(self):
        # Get text from app written by user
        user_input_from_chat = self.manager.current_screen.ids.user_input.text
        # List of image urls (wikipedia)
        pages = wikipedia.page(user_input_from_chat)
        # Give a first image url on the list
        image_urls = pages.images[0]   
        # Download the image
        req = requests.get(image_urls)
        time.sleep(10)
        picpath = r"image.png"
        with open(picpath, 'wb') as pic:
            pic.write(req.content)
        
        # Show image on the app
        self.manager.current_screen.ids.image_for_screen.source = picpath

class RootWidgets(ScreenManager):
    """Create the manager"""
    
    pass
    
class App(App):
    """This class is a child class from the kivy App class."""
    
    def build(self):
        return RootWidgets()
    

App().run()