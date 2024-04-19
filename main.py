import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player=Player()#
scoreboard=Scoreboard()
cars=[]
#####
import  random
def generate_cars():
    for _ in range(5):
        new_car =CarManager()
        new_x=random.randint(320,420)
        new_y=random.randint(-250,250)
        new_car.goto(new_x, new_y)
        cars.append(new_car)


screen.listen() #
screen.onkey(player.up, "Up") #

generate_factor=0

game_is_on = True
while game_is_on:
    time.sleep(0.1)

    ####
    if generate_factor==0 or generate_factor==40:
        generate_cars()
        generate_factor=0

    for car in cars:
        car.move()
        if car.xcor() <= 10 and car.xcor() >= -10 and player.distance(car)<20:
            scoreboard.game_over()
            game_is_on=False

        if player.destination():
            player.initial_position()
            car.speed_up()
            scoreboard.level_up()







    generate_factor+=1





    screen.update() #eno

screen.exitonclick()