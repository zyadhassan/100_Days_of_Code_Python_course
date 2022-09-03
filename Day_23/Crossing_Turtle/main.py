import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from ScoreBoard import Scoreboard2

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.title("Cross Turtle Game v1.0")  # the title of the window

player1=Player()
cars=CarManager()
board=Scoreboard2()

# Listen Events
screen.listen()
screen.onkeypress(player1.move,'Up')

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    if player1.Level_Up():
        cars.Level_up_car()
        board.increase()

    if cars.hit(player1):
        game_is_on=False
        board.game_over()
    cars.move_car()


screen.exitonclick()