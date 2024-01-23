from turtle import Turtle, Screen
import random

is_race_on = False
feer = Screen()
feer.setup(width=500, height=400)
user_bet = feer.textinput(title="Make your bet", prompt='Which turtle will win the race? \n"red", "orange", "yellow", "green", "blue", "indigo", "violet": ')

jack = Turtle()
jack.ht()
jack.penup()
jack.goto(x=230, y=-100)
jack.pendown()
jack.setheading(90)
jack.forward(220)

colors = ["red", "orange", "yellow", "green", "blue", "indigo", "violet"]
fin = [-80, -50, -20, 10, 40, 70, 100]
turtles = []
for tim in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(colors[tim])
    new_turtle.goto(x=-230, y=fin[tim])
    turtles.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in turtles:
        if turtle.xcor() > 210:
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle is the winner.")
            else:
                print(f"You've lost! The {winning_color} turtle is the winner.")
            is_race_on = False

        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)



feer.exitonclick()