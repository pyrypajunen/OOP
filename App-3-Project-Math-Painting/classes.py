##### IMPORTS ##### 
import numpy as np
from PIL import Image

class Canvas:
    """Object where all shapes are going to be drawn."""
    
    def __init__(self, height, width, color):
        self.height = height
        self.width = width
        self.color = color
        
        # Creating 3d numpy array
        self.data = np.zeros((self.height, self.width, 3), dtype=np.uint8)
        # Change the color by user
        self.data[:] = self.color
        
    def make(self,path_of_image):
        """ Converts the current array into an image file """
        img = Image.fromarray(self.data, 'RGB')
        img.save(path_of_image)

"""Rectangle, Circle and Square classas makes shapes of the images """
class Rectangle:
    
    def __init__(self,x, y, height, width, color):
        self.x = x
        self.y = y
        self.height = height
        self.width = width
        self.color = color
        
    def draw(self, canvas):
        """ Draws into the canvas"""
        canvas.data[self.x: self.x + self.height, self.y:: self.y + self.width] = self.color
    
class Circle:
    
    def __init__(self,x, y, z, color):
        self.x = x
        self.y = y
        self.z = z
        self.color = color
        
    def draw(self, color):
        pass
    

class Square:
    
    def __init__(self, x, y, side , color):
        self.x = x
        self.y = y
        self.side = side
        self.color = color
        
    def draw(self, canvas):
        """ Draws into the canvas"""
        canvas.data[self.x: self.x + self.side, self.y:: self.y + self.side] = self.color
