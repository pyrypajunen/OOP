# Importing the classes and creating the CLI interface 
from classes import Canvas, Rectangle, Square


# Get canvas size from user
canvas_width = int(input("Give a canvas width: "))
canvas_height = int(input("Give a canvas height: "))

# Dictionary of color codes
colors = {"white" :(255, 255, 255), "black" : (0, 0, 0)}
canvas_color = input("Give a canvas color (black or white): ")

# Create the canvas with user inputs

canvas = Canvas(height=canvas_height, width=canvas_width, color=colors[canvas_color])

while True:
    shape = input("What do you like to draw? Rectangle, Square? Enter q to quit. ")
    # Ask rectangle data and create rectangle
    if shape.lower() == "rectangle":
        rectangle_x = int(input("Enter x of the rectangle: "))
        rectangle_y = int(input("Enter y of the rectangle: "))
        rectangle_width = int(input("Enter the width of the rectangle: "))
        rectangle_height = int(input("Enter the height of the rectangle: "))
        rectangle_red = int(input("How much red should be used in the rectangle? "))
        rectangle_green = int(input("How much green? "))
        rectangle_blue = int(input("How much blue? "))
        
        # Create the rectangle
        rectangle = Rectangle(x=rectangle_x, y=rectangle_y, width=rectangle_width, height= rectangle_height,
                              color = (rectangle_red, rectangle_green, rectangle_blue))
        rectangle.draw(canvas)    
        
    if shape.lower() == "square":
        square_x = int(input("Enter x of the square: "))
        square_y = int(input("Enter y of the square: "))
        square_side = int(input("Enter the side length of the square: "))
        square_red = int(input("How much red should be used in the square? "))
        square_green = int(input("How much green? "))
        square_blue = int(input("How much blue? "))
                       
        square = Square(x = square_x, y = square_y, side= square_side, 
                        color = (square_red, square_green, square_blue))
        square.draw(canvas)
    
    if shape.lower() == "q":
        break
    
canvas.make('canvas.png')