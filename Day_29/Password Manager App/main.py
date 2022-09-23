from tkinter import *
FONT_NAME = "Courier"
from tkinter import messagebox
import pyperclip
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
import random
def gen_Password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
    password=""
    pass_list=[]
    for num in range (random.randint(2,4)):
        pass_list.append(random.choice(numbers))
    for sympol in range (random.randint(2,4)):
        pass_list.append(random.choice(symbols))
    for letter in range (random.randint(8,10)):
        pass_list.append(random.choice(letters))

    random.shuffle(pass_list)
    password="".join(pass_list)
    Password_entry.delete(0,END)
    Password_entry.insert(0,password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save(web,mail,password):
    with open("data.text","a") as file:
        file.writelines(f"{web} | {mail} | {password}\n")

def add_but():
    password = Password_entry.get()
    mail = Username_entry.get()
    web = Website_entry.get()
    if len(password)==0 or len(mail)==0 or len(web)==0:
        messagebox.showwarning(title="Oops",message="Make sure you don't left any field empty")
    else:
        is_ok = messagebox.askokcancel(title=web,message=f"The details you have Entered :\nEmail/Username: {mail}\n"
                                                         f"Password : {password}\nIs it ok to save?\n")

        if is_ok:
            save(web=web,mail=mail,password=password)
            Password_entry.delete(0,END)
            Website_entry.delete(0,END)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager App")
window.config(pady=20 ,padx=20)


#Canvas LOGO
widget = Canvas(width=200,height=200)
photo = PhotoImage(file="logo.png")
widget.create_image(100,100,image=photo)
widget.grid(row=0,column=1)

# Label Website name
Website_label = Label(text="Website:")
Website_label.grid(column=0,row=1)


# Entry Website
Website_entry = Entry(width=35)
Website_entry.focus()
Website_entry.grid(row=1,column=1,columnspan=2,sticky=EW)


# Label Email
Username_label = Label(text="E-mail/Username:")
Username_label.grid(column=0,row=2)


# Entry Email
Username_entry = Entry(width=35)
Username_entry.insert(END,"zyad_hassan_2020@outlook.com")
Username_entry.grid(row=2,column=1,columnspan=2,sticky=EW)

# Label Password
Password_label = Label(text="Password:")
Password_label.grid(column=0,row=3)


# Entry Password
Password_entry = Entry(width=21)
Password_entry.grid(row=3,column=1,sticky=EW)

# Button Generate Password
pass_gen = Button(text="Generate Password",command=gen_Password)
pass_gen.grid(row=3,column=2)

# Button ADD Password
pass_add = Button(text="Add Password",width=36,command=add_but)
pass_add.grid(row=4,column=1,columnspan=2,sticky=EW)



window.mainloop()