from turtle import Turtle, Screen


# Functions


def move_forwards():
   timmy.forward(10)


def move_backwards():
   timmy.backward(10)


def round_clockwise():
   timmy.right(5)


def round_anticlockwise():
   timmy.left(5)


def clear_draw():
    timmy.setpos(0, 0)
    timmy.setheading(0)
    timmy.clear()

# define the turtle object and Screen object
timmy = Turtle()
screen = Screen()
# define the screen to listen to an event

screen.listen()
screen.onkeypress(fun=move_forwards, key="w")
screen.onkeypress(fun=clear_draw, key="c")
screen.onkeypress(fun=move_backwards, key="s")
screen.onkeypress(fun=round_clockwise, key="d")
screen.onkeypress(fun=round_anticlockwise, key="a")

screen.exitonclick()