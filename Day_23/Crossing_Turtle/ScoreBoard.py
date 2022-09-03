FONT = ("Courier", 24, "normal")

from turtle import Turtle

class Scoreboard2(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color("black")
        self.goto(x=-200, y=250)
        self.level = 1
        self.write(f"level: {self.level} ", align='center', font=FONT)

    def increase(self):
        self.level+=1
        self.clear()
        self.write(f"level: {self.level} ", align='center', font=FONT)

    def game_over(self):
        self.goto(0,0)
        self.write(f"GAME OVER. ", align='center', font=('Courier', 36, 'normal'))