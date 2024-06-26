STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280

from turtle import Turtle

class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.setheading(90)
        self.penup()
        self.initial_position()

    def up(self):
        new_y= self.ycor() + 10
        self.goto(self.xcor(), new_y)

    def destination(self):
        if self.ycor()==FINISH_LINE_Y:
            return True
        else:
            return False
    def initial_position(self):
        self.goto(STARTING_POSITION)