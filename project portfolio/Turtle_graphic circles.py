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

jin.speed(0)
jin.ht()
jin.width(1)
def painting(gap):
    for _ in range(int(360/ gap)):
        color_change()
        jin.circle(100)
        jin.left(gap)

painting(5)

dir = Screen()
dir.exitonclick()