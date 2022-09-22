from tkinter import *



# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps=0

#Check Marks
mark="✔"
check_mark=""


# State
state="Start"
run=False
work=False
# ---------------------------- TIMER RESET ------------------------------- # 
def reset():
    global run
    global work
    global check_mark
    global reps
    reps=0
    check_mark=""
    run =False
    canvas.itemconfig(timer_text,text="00:00")
    Label_state.config(text="Start",fg=GREEN)
    Label_Check.config(text=check_mark)
    work=False
# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global work
    if not work :
        work=True
        global run
        run=True
        global check_mark
        global reps
        if reps%2 ==0 and reps!=8 :
            Label_state.config(text="Work",fg=GREEN)
            count_down(WORK_MIN*60)
        elif reps==1 or reps ==3 or reps==5 :
            Label_state.config(text="Break", fg=PINK)
            count_down(SHORT_BREAK_MIN*60)

        elif reps==7:
            Label_state.config(text="Break", fg=RED)
            count_down(LONG_BREAK_MIN*60)
        else:
            reps=0
            check_mark=""
        reps += 1

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    global mark
    global reps
    global run
    global work
    global check_mark
    count_min=count//60
    count_sec=count%60
    if count_sec<10:
        count_sec=f"0{count_sec}"
    if count_min<10:
        count_min=f"0{count_min}"
    if run:
        canvas.itemconfig(timer_text,text=f"{count_min}:{count_sec}")
        if count >0:
            window.after(1000,count_down,count-1)
        else:
            if reps%2!=0:
                check_mark += mark
                Label_Check.config(text=check_mark)
            work=False
            start_timer()


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro Foucs App")
window.config(pady=100,padx=100)
window.config(bg=YELLOW)

# Canvas widget in the screen
canvas= Canvas(width=205,height=224,bg=YELLOW,highlightthickness=0)
# image in Canves
photo=PhotoImage(file="tomato.png")
canvas.create_image(100,112,image=photo)
# text in canvas
timer_text=canvas.create_text(100,130,text=f"00:00",font=(FONT_NAME,35,"bold"),fill=("white"))
canvas.grid(row=1,column=1)


#Label Timer
Label_state = Label(text=f"{state}", font=(FONT_NAME,50),fg=GREEN,bg=YELLOW)
Label_state.grid(row=0,column=1)

# Button -----> Start
start_button=Button(text="Start",padx=5,pady=5,command=start_timer)
start_button.grid(row=2,column=0)

# Button -----> Reset
reset_button=Button(text="Reset",padx=5,pady=5,command=reset)
reset_button.grid(row=2,column=2)

#Label Check mark
Label_Check = Label(text=check_mark, font=(FONT_NAME,10,"bold"),fg=GREEN,bg=YELLOW)
Label_Check.grid(row=3,column=1)



window.mainloop()
