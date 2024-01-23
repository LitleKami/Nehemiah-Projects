from turtle import Screen, Turtle
from paddle import Paddle
#from ball import Ball
#from scoreboard import Scoreboard
import time

position_1 = [(-240, 10), (-240, 0), (-240, -10)]
position_2 = [(280, 10), (280, 0), (280, -10)]

screen = Screen()
screen.setup(600, 600)
screen.bgcolor("black")
screen.title("litle_kami Pong")
screen.tracer()

paddle_1 = Paddle(position_1)
paddle_2 = Paddle(position_2)
#ball = Ball()
#scoreboard_1 = Scoreboard()
#scoreboard_2 = Scoreboard()
#scoreboard_1.goto(-50, 200)
#scoreboard_2.goto(50, 200)


screen.listen()
screen.onkeypress(paddle_1.move_up, "Up")
screen.onkeypress(paddle_1.move_down, "Down")
#screen.onkey(paddle_2.move_up, "Up")
#screen.onkey(paddle_2.move_down, "Down")
#paddle_1.move_up()
screen.update()
time.sleep(0.1)


screen.exitonclick()
