from turtle import Turtle, Screen
import random


# define the screen
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your choice", prompt="Which turtle will win the race ? Enter a color : ")



# define the turtles

colors=['red','orange','yellow','green','blue','purple']
turtles=['t1','t2','t3','t4','t5','t6']
objects={}

for i in range(6):
    objects[turtles[i]]=Turtle(shape="turtle")
    objects[turtles[i]].penup()
    objects[turtles[i]].color(colors[i])
    objects[turtles[i]].goto(x=-230,y=(90-(i*30)))
# Race Game
winner=""
race_is_on = False
if user_bet:
    race_is_on=True

while race_is_on:
    for t in turtles:
        objects[t].forward(random.randint(0,10))

    for t in turtles:
       if objects[t].pos()[0]>230 :
            winner=objects[t].color()[0]
            race_is_on=False

if(user_bet==winner):
    print(f"you win !! the {winner} turtle won the race")
else:
    print(f"you lose !! the {winner} turtle won the race")

# close the screen
screen.exitonclick()










