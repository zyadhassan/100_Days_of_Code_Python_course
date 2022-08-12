from turtle import Turtle , Screen
import random
import turtle


# Color Random Gen function
def rand_RGB():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    tuple = (r, g, b)
    return tuple


# define function to draw shape
def turtle_shape(turt, steps, sides, dash):
    for i in range(sides):
        if dash:
            dash_line(turt, steps)
        else:
            turt.fd(steps)
        turt.left(360/sides)


# define function to draw dash line
def dash_line(tur, steps):
    step = steps/10
    step = round(step/2)
    for i in range(step):
        tur.penup()
        tur.fd(10)
        tur.pendown()
        tur.fd(10)


# define function to random walk
def random_walk(t,steps):
    t.speed(10)
    t.pensize(15)
    for i in range(round(steps/30)):
        t.color(rand_RGB())
        t.setheading(random.randint(0, 3)*90)
        t.fd(30)


# define Spirograph function
def Spirograph(turt, radius ,color, gap):
    turt.speed(11)
    for i in range(int(360/gap)):
        if color:
            turt.color(rand_RGB())
        turt.circle(radius)
        turt.setheading(i*gap)
    turt.setheading(0)

# define turtle object
timmy = Turtle()
timmy.shape("turtle")


# to work with RGB put colormode of the file turtle equal 255
turtle.colormode(255)

#for i in range(3, 11):
#    timmy.color(rand_RGB())
#    turtle_shape(turt=timmy, steps=100, sides=i, dash=False)


#random_walk(timmy, 200*30)


Spirograph(turt=timmy, radius=100 ,color=True,gap=10)
timmy.fd(200)
Spirograph(turt=timmy, radius=100 ,color=True,gap=10)

# define Screen to show
scr1 = Screen()
scr1.exitonclick()
