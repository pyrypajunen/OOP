from random import randint
import turtle

class Point:
    
    def __init__(self,x ,y):
        self.x = x
        self.y = y

    #Method for comparing coordinates
    def falls_in_rectangle(self, rectangle):
        if rectangle.point1.x < self.x \
        < rectangle.point2.x \
        and rectangle.point1.y < self.y \
        < rectangle.point2.y:
            return True
        else:
            return False

class Rectangle:

    def __init__(self, point1, point2):
        self.point1 = point1
        self.point2 = point2

    #method for calculating area of coordinates
    def area(self):
        return (self.point2.x - self.point1.x ) * \
        (self.point2.y - self.point1.x)

#making a new class and inherit the Rectangle class to it
class GuiRectangle(Rectangle):

    def draw(self, canvas):
        canvas.penup()
        canvas.goto(self.point1.x, self.point1.y) #coordinates from rectangle class

        canvas.pendown()
        canvas.forward(self.point2.x - self.point1.x) #Drawing left to right
        canvas.left(90) #turn 90 degrees left
        canvas.forward(self.point2.y - self.point1.y) #Drawing down to up
        canvas.left(90)
        canvas.forward(self.point2.x - self.point1.x) #Drwaing right to left
        canvas.left(90)
        canvas.forward(self.point2.y - self.point1.y) #Drawing up to down


class GuiPoint(Point):

    def draw(self, canvas, size = 15, color = "red"):
        canvas.penup()
        canvas.goto(self.x, self.y)
        canvas.pendown()
        canvas.dot(size, color)

        
#Chosing random ints
gui_rectangle = GuiRectangle(Point(randint(0, 400), randint(0, 400)),
    Point(randint(10, 400), randint(10,400)))

#Chosing random coordinates
rectangle = GuiRectangle(Point(randint(0, 400), randint(0, 400)),
    Point(randint(10, 400), randint(10, 400))) 

print("Rectangle Coordinates:",
    rectangle.point1.x, ",",
    rectangle.point1.y, "and",
    rectangle.point2.x, ",",
    rectangle.point2.y)

#Ask coordinates from user
user_point = GuiPoint(float(input("Guess X coord: ")),
    float(input("Guess Y coord: "))) 

user_area = float(input("Guess rectangle area: "))

print("Your point was inside rectangle: ",
    user_point.falls_in_rectangle(rectangle))
print("Your area was off by: ", rectangle.area() - user_area)

# Create a canvas instance
myturtle = turtle.Turtle()
gui_rectangle.draw(canvas=myturtle)
user_point.draw(canvas=myturtle)
turtle.done()
