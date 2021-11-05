# Importing the classes and creating the CLI interface 
from classes import Canvas, Rectangle, Circle, Square


# Get canvas size from user
canvas_width = int(input("Give a canvas width: "))
canvas_height = int(input("Give a canvas height: "))

# Dictionary of color codes
colors = {"white" :(255, 255, 255), "black" : (0, 0, 0)}
canvas_color = input("Give a canvas color (black or white): ")

# Create the canvas with user inputs

canvas = Canvas(height=canvas_height, width=canvas_width, color=colors[canvas_color])

while True:
    shape = input("What do you like to draw? Rectangle, Square or circle? Enter q to quit. ")
    # Ask rectangle data and create rectangle
    if shape.lower() == "rectangle":
        #Ask datas
        # x, y, width, height, red, greed, blue 
        rectangle = Rectangle()
        pass
    
    if shape.lower() == "square":
        #Ask datas
        square = Square()
    
    if shape.lower() == "circle":
        circle = Circle()# instance of Circle
        pass
    
    
    if shape.lower() == "quit":
        break
    
canvas.make('canvas.png')