import colorgram
# Extract colors from image
colors = colorgram.extract('hirst_paint.jpg', 30)

# list of colors RGB
color_list = []
for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    color_list.append((r, g, b))


# deleting white colors
color_list=[(236, 224, 80), (197, 7, 71), (195, 164, 13), (201, 75, 15),
 (231, 54, 132), (110, 179, 216), (217, 163, 101), (27, 105, 168), (35, 186, 109), (19, 29, 168), (13, 23, 66), (212, 135, 177),
 (233, 223, 7), (199, 33, 132), (13, 183, 212), (230, 166, 199), (126, 189, 162), (8, 49, 28), (40, 132, 77),
 (128, 219, 232), (58, 12, 25), (67, 22, 7), (114, 90, 210), (146, 216, 199), (179, 17, 8), (233, 66, 34)]


from turtle import Turtle , Screen
import random
import turtle
import math


# define function to paint
def hirst(turt,gap = 50, dot_width_count = 10, dot_hight_count =10 ):
    turt.hideturtle()
    turt.speed(20)
    turt.penup()
    turt.setheading(220)
    turt.fd(350)
    turt.setheading(0)
    for i in range(dot_hight_count):
        postiton = turt.position()
        for i in range(dot_width_count):
            colo=random.choice(color_list)
            turt.dot(20,colo)
            turt.fd(gap)
        turt.setpos(postiton)
        turt.setheading(90)
        turt.fd(gap)
        turt.setheading(0)


# to work with RGB put colormode of the file turtle equal 255
turtle.colormode(255)


# define turtle object
timmy = Turtle()

# call the function to print
hirst(timmy,50)

# define Screen to show
scr1 = Screen()
scr1.exitonclick()
