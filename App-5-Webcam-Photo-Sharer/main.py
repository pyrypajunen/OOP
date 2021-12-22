### IMPORTS ###
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.clipboard import Clipboard
from kivy.lang import Builder
import cv2
import time
import webbrowser
from filestack import Client

Builder.load_file('frontend.kv')

    
class WebcamScreen(Screen):
    
    def start_webcam(self):
        """Starts camera and change button text"""
        self.ids.camera.play = True
        self.ids.button.text = 'Stop Webcam'
        self.ids.camera.texture = self.ids.camera._camera.texture
        
    def stop_webcam(self):
        """Stops the webcam and changes the button text"""
        self.ids.camera.play = False
        self.ids.button.text = 'Start Webcam'
        self.ids.camera.texture = None
    
    def capture_method(self):
        """Creates a filename with the current time and save the photo"""
        current_time = time.strftime('%Y%m%d-%H%M%S')
        self.picpath = f"App-5-Webcam-Photo-Sharer/files/{current_time}.png"
        self.ids.camera.export_to_png(self.picpath) # Will contain generated image path
        self.manager.current = 'photo_screen'
        self.manager.current_screen.ids.image.source = self.picpath
        
        
    
   
class PhotoScreen(Screen):
    link_msg = "Create a link first!"
    def create_link(self):
            """Accesses the photo path, upload in to the web,
            inserts the link in the label widget"""
            filepath = App.get_running_app().root.ids.camera_screen.picpath
            fileshare = FileSharer(picpath= filepath)
            self.url = fileshare.share()
            self.ids.link.text = self.url
            
    def copylink(self): 
        """Copy link to clipboard"""
        try:
            Clipboard.copy(self.url)
        except:
            self.ids.link.text = self.link_msg
            
    def open_link(self):
        """Open link with browser"""
        try:
            webbrowser.open(self.url)
        except:
            self.ids.link.text = self.link_msg
            

class FileSharer:
    
    def __init__(self,picpath, api_key = "AYKRYd4S9S2CgT65pFb5Vz"):
        self.picpath = picpath
        self.api_key = api_key # Personal API key from filestack
        
        
    def share(self):
        client = Client(self.api_key)
        new_filelink = client.upload(filepath = self.picpath) # uploading the file
        return new_filelink.url
            
    
class RootWidgets(ScreenManager):
    """Create the manager"""
    pass
    
class MainApp(App):
    """This class is a child class from the kivy App class."""
    
    def build(self):
        return RootWidgets()
    

MainApp().run()

