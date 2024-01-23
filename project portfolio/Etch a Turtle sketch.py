from turtle import Turtle, Screen

gen = Turtle()
tim = Screen()

def move_forward():
    gen.forward(10)
def turn_left():
    gen.left(90)
def turn_right():
    gen.right(90)
def home():
    gen.home()
def clearscreen():
    gen.clear()

tim.listen()
tim.onkey(fun=move_forward, key="space")
tim.onkey(fun=turn_left, key="l")
tim.onkey(fun=turn_right, key="r")

tim.exitonclick()
