import turtle

import pandas
import pandas as pd

# Define The Screen
screen = turtle.Screen()
screen.title("US State Quiz ")


image = "blank_states_img.gif"
screen.addshape(image)

turtle.shape(image)

# define turtle
pen=turtle.Turtle()
pen.hideturtle()
pen.penup()

# CSV File
data=pd.read_csv("50_states.csv")

# Write fun

def write_state(state):
    x=data[data.state==user_text].x
    y=data[data.state==user_text].y
    pen.goto(int(x),int(y))
    pen.write(f"{user_text}",align='center', font=('Courier', 6, 'normal'))

states=data.state.to_list()
count=0
game_on=True
gussed_state=[]
# main loop
while(game_on):
    user_text=screen.textinput(title=f"{count}/50 Guess The State", prompt="What's another state's name ?")
    user_text=str(user_text).capitalize()
    if user_text =="Exit" or count==50 :
        game_on=False

    for state in states:
        if state==user_text:
            count += 1
            gussed_state.append(state)
            write_state(state)
            continue


miss_state=[]
for state in states:
    flag_exist=False
    for s in gussed_state:
        if s==state:
            flag_exist=True
            break
    if(not flag_exist):
        miss_state.append(state)

df=pandas.DataFrame({"State":miss_state})
df.to_csv("Miss_States")

















# Keep Screen open
turtle.mainloop()
