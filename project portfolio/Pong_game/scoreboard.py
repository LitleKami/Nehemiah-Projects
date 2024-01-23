from turtle import Turtle

FONT = ("arial", 20, "bold")
POSITION = "center"

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.shapesize(0.5, 0.5)
        self.ht()
        self.penup()
        self.color("white")
        self.write(f"{self.score}", False, POSITION, FONT)

    def update_score(self):
        self.clear()
