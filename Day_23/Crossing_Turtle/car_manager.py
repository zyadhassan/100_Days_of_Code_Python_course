COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
from turtle import Turtle
import random


class CarManager:
    def __init__(self):
        self.Cars=[]
        self.move_dis=STARTING_MOVE_DISTANCE
        for i in range(15):
            car=Turtle("square")
            car.penup()
            car.setheading(180)
            car.color(random.choice(COLORS))
            car.shapesize(stretch_wid=1,stretch_len=2)
            car.setposition(x=random.randint(-200,300),y=-240+i*25 )
            self.Cars.append(car)


    def move_car(self):
        for car in self.Cars:
            car.setposition(x=car.xcor()-self.move_dis,y=car.ycor())
            if car.xcor()<-300:
                car.setposition(x=300,y=random.randint(-240,280))
    def Level_up_car(self):
        self.move_dis+=MOVE_INCREMENT

    def hit(self,player):
        for car in self.Cars:
            if player.distance(car) < 23 :
                return True

        return False
