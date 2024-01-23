import turtle
from turtle import *
import random

turtle.colormode(255)
jin = Turtle()
jin.shape("turtle")
#jin.ht()
def color_change():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    jin.color(r, g, b)

direction = [90, 180, 270, 360]

jin.width(10)
jin.shapesize(1)
jin.speed(1)
for _ in range(300):
    jin.setheading(random.choice(direction))
    jin.forward(25)
    color_change()

screen = Screen()
screen.exitonclick()
