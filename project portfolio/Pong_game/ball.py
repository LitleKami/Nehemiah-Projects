from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shapesize(0.5, 0.5)
        self.penup()
        self.color("white")
