### IMPORTS ###
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder
import cv2
import time

Builder.load_file('frontend.kv')

    
class WebcamScreen(Screen):
    
    def start_webcam(self):
        self.ids.camera.play = True
        self.ids.button.text = 'Stop Webcam'
        self.ids.camera.texture = self.ids.camera._camera.texture
        
    def stop_webcam(self):
        self.ids.camera.play = False
        self.ids.button.text = 'Start Webcam'
        self.ids.camera.texture = None
    
    def capture_method(self):
        current_time = time.strftime('%Y%m%d-%H%M%S')
        picpath = f"App-5-Webcam-Photo-Sharer/images/{current_time}.png"
        self.ids.camera.export_to_png(picpath)
        self.manager.current = 'photo_screen'
        self.manager.current_screen.ids.image.source = picpath
    
   
class PhotoScreen(Screen):
    
    def filepath(self):
        pass
    
    def api(self):
        pass
    
    def share_photo(self):
        pass
    
    
class PhotoSharer:
    
    def __init__(self, photopath, api_key = ""):
        self.photopath = photopath
        self.api_key = api_key
        
    def share_photo(self) -> str:

        client = Client(self.api_key)
        new_filelink = client.share_photo( photopath = self.photopath)
        return new_filelink.url
    
class RootWidgets(ScreenManager):
    """Create the manager"""
    pass
    
class MainApp(App):
    """This class is a child class from the kivy App class."""
    
    def build(self):
        return RootWidgets()
    

MainApp().run()

