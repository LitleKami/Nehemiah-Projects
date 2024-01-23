from turtle import Turtle
import random


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shapesize(0.4, 0.4)
        self.penup()
        self.shape("turtle")
        self.color("blue")
        self.speed(0)
        self.refresh()


    def refresh(self):
        x_cor = random.randint(-280, 280)
        y_cor = random.randint(-280, 250)
        self.goto(x_cor, y_cor)
