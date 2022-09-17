import tkinter
import random

def convert_ms_kh():
    speed=0
    speed=ms_input.get()
    speed=float(speed)*3.6
    labe_result.config(text=str(speed))



#window
window = tkinter.Tk()
window.title("Speed Converter")
window.minsize(width=200,height=100)
window.config(padx=30,pady=30)


#input ms
ms_input=tkinter.Entry(width=5)
ms_input.grid(column=1,row=0)

label_ms=tkinter.Label(text="m/s")
label_ms.grid(column=2,row=0)
label_ms.config(pady=5,padx=5)


label_equal=tkinter.Label(text="is equal to ")
label_equal.grid(column=0,row=1)
label_equal.config(pady=5,padx=5)

#input kh

labe_result=tkinter.Label(text="0")
labe_result.config(pady=5,padx=5)
labe_result.grid(column=1,row=1)

label_kh=tkinter.Label(text="k/h")
label_kh.grid(column=2,row=1)
label_kh.config(pady=5,padx=5)

#button
conv_button = tkinter.Button(text="Convert",command=convert_ms_kh)
conv_button.config(padx=5,pady=5)
conv_button.grid(column=1,row=2)



window.mainloop()