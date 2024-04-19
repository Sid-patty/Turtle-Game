COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

from turtle import Turtle
import random
class CarManager(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("square")
        self.color(random.choice(COLORS))
        self.penup()
        self.shapesize(stretch_wid=1, stretch_len=2)
        self.velocity=0

    def move(self):
        self.backward(self.velocity + STARTING_MOVE_DISTANCE)

    def speed_up(self):
        self.velocity+=MOVE_INCREMENT
