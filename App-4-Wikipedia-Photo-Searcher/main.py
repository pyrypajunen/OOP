### IMPORTS ###
import wikipedia
import urllib
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder

# Loading frontend file
Builder.load_file('frontend.kv')

class ScreenOne(Screen):
    """Creating dynamic wikipedia image changer method"""
    
    def user_input(self) -> str:
        user_input_from_chat = self.manager.current_screen.ids.user_input.text
        return user_input_from_chat
    
    def search_img_url(self) -> str:
        # Get text from app written by user
        # List of image urls (wikipedia)
        page = wikipedia.page(self.user_input())
        # Give a first image url on the list
        image_urls = page.images[0]
        return image_urls
    
    def download_image(self) -> str:  
        # Download the image
        response = urllib.request.urlopen(self.search_img_url())
        # Choosing file path (where image will be downloaded) and image name
        picname =  r'App-4-Wikipedia-Photo-Searcher\images\ ' + self.user_input() + '.JPG'
        with open(picname, 'wb') as pic:
            pic.write(response.read())
        return picname
    
    def image_set(self):
        # Show image on the app
        self.manager.current_screen.ids.image_for_screen.source = self.download_image()

class RootWidgets(ScreenManager):
    """Create the manager"""
    pass
    
class MainApp(App):
    """This class is a child class from the kivy App class."""
    
    def build(self):
        return RootWidgets()
    

MainApp().run()

