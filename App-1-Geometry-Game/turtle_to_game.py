# Using this for drawing a rectangle
import turtle

myturtle = turtle.Turtle()

# Go to a certain coordinate
myturtle.penup()
myturtle.goto()

myturtle.pendown()
myturtle.forward(100)
myturtle.left(90)

myturtle.forward(200)
myturtle.left(90)

myturtle.forward(100)
myturtle.left(90)
myturtle.forward(200)

turtle.done()