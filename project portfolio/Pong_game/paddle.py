from turtle import Turtle

MOVE_DISTANCE = 10

class Paddle():
    def __init__(self, segments):
        self.pads = []
        self.paddle(segments)
        self.head = self.pads[0]
        self.tail = self.pads[-1]

    def paddle(self, segments):
        for segment in segments:
            pad = Turtle()
            pad.shape("square")
            pad.color("white")
            pad.turtlesize(0.5)
            pad.penup()
            pad.setposition(segment)
            pad.setheading(90)
            self.pads.append(pad)

    def move_up(self):
        for pad_num in range(len(self.pads) - 1, 0, -1):
            new_x = self.pads[pad_num - 1].xcor()
            new_y = self.pads[pad_num - 1].ycor()
            self.pads[pad_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def move_down(self):
        for pad_num in range(0, len(self.pads) - 1, -1):
            new_x = self.pads[pad_num - 2].xcor()
            new_y = self.pads[pad_num - 2].ycor()
            self.pads[pad_num].goto(new_x, new_y)
        self.tail.backward(MOVE_DISTANCE)

    def position_1(self):
        pass

