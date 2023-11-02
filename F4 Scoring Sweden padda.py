import tkinter
from tkinter import ttk
from tkinter import messagebox
import sqlite3



def judges_data():

   # user_info_frame = tkinter.LabelFrame(frame, text="Put in Judge Nr and name")
    user_info_frame.config(text="Put in Judge Nr and name")
    user_info_frame.grid(row=0, column=0, padx=20, pady=10)

    # Create a variable to hold the selected option
    radio_var = tkinter.StringVar(value="1")

    # Create Radiobuttons
    radio_button1 = tkinter.Radiobutton(user_info_frame, text="Judge 1", variable=radio_var, value="1")
    radio_button1.grid(row=0, column=0)
    radio_button2 = tkinter.Radiobutton(user_info_frame, text="Judge 2", variable=radio_var, value="2")
    radio_button2.grid(row=0, column=1)
    radio_button3 = tkinter.Radiobutton(user_info_frame, text="Judge 3", variable=radio_var, value="3")
    radio_button3.grid(row=0, column=2)
    # Pack the Radiobuttons
    first_name_label = tkinter.Label(user_info_frame, text="Name", width=20)
    first_name_label.grid(row=1, column=1)
    first_name_entry = tkinter.Entry(user_info_frame)
    first_name_entry.grid(row=2, column=1)

    for widget in user_info_frame.winfo_children():
        widget.grid_configure(padx=10, pady=5)
    startbutton2.grid_forget()
    startbutton.grid_forget()

    nextbutton = tkinter.Button(user_info_frame, text="Next", width=20, command=startnummer)
    nextbutton.grid(row=2, column=2)






def startnummer():
     user_info_frame.destroy()
     startbutton2.destroy()
     startbutton.destroy()
     startnummerlabel.config(text="Start Nr:")
     startnummerlabel.grid(row=0, column=0)
     startnummer2label.config(text="1")
     startnummer2label.grid(row=0, column=1)
     roundnummerlabel.config(text="Round Nr:")
     roundnummerlabel.grid(row=1, column=0)
     roundnummerlabel2.config(text="2")
     roundnummerlabel2.grid(row=1, column=1)
     startcompetition.config(text="start Round", command=judgepoint)
     startcompetition.grid(row=2, column=2)




def judgepoint():


    startnummerlabel.grid_forget()
    startnummer2label.grid_forget()
    roundnummerlabel.grid_forget()
    roundnummerlabel2.grid_forget()
    startcompetition.grid_forget()
    Stortminus  = tkinter.Button(window, font=('Times', 48))
    Stortminus ["bg"] = "#fb5050"
    Stortminus["fg"] = "#000000"
    Stortminus ["justify"] = "center"
    Stortminus ["text"] = "-"
    Stortminus .place(x=0, y=110, width=312, height=314)
    Stortminus ["command"] = spinminus


    manresult.config (text= str(x), font=('Times', 20))
    manresult["borderwidth"] = "1px"
    manresult["fg"] = "#333333"
    manresult["justify"] = "center"
    manresult.place(x=320, y=110, width=291, height=315)

    Stortplus = tkinter.Button(window, font=('Times', 48))
    Stortplus["bg"] = "#87fb3a"
    Stortplus["fg"] = "#000000"
    Stortplus["justify"] = "center"
    Stortplus["text"] = "+"
    Stortplus.place(x=620, y=110, width=271, height=312)
    Stortplus["command"] = spinplus

    GLabel_247 = tkinter.Label(window, font=('Times', 18))
    GLabel_247["fg"] = "#333333"
    GLabel_247["justify"] = "center"
    GLabel_247["text"] = "Startnr:"
    GLabel_247.place(x=20, y=40, width=70, height=25)

    GLabel_483 = tkinter.Label(window, font=('Times', 18))
    GLabel_483["fg"] = "#333333"
    GLabel_483["justify"] = "center"
    GLabel_483["text"] = "10"
    GLabel_483.place(x=90, y=40, width=30, height=30)

    GLabel_2 = tkinter.Label(window, font=('Times', 18))
    GLabel_2["fg"] = "#333333"
    GLabel_2["justify"] = "center"
    GLabel_2["text"] = "Pilot:"
    GLabel_2.place(x=200, y=40, width=70, height=25)

    GLabel_437 = tkinter.Label(window, font=('Times', 18), justify="left")
    GLabel_437["fg"] = "#333333"
    GLabel_437["text"] = "Otto"
    GLabel_437.place(x=270, y=40, width=195, height=30)


def spinplus():
    global x
    if x<=9.5:
     x +=0.5
     manresult.config(text=str(x), font=('Times', 20))






def spinminus  ():
    global x
    if x >= 0.5:
        x -= 0.5
        manresult.config(text=str(x), font=('Times', 20))


window = tkinter.Tk()
window.title("judges info")
width = 900
height = 600
window.geometry('900x600')
frame = tkinter.Frame(master=window)
window.resizable(False, False)
frame.pack()


runonce ="0"
if runonce=="0":

    startbutton = tkinter.Button(frame, text="ny tävling", command=judges_data, width=20, height=10, font=('Arial', 13))
    startbutton.grid(row=1, column=0)

    startbutton2 = tkinter.Button(frame, text="sparad tävling", command=startnummer, width=20, height=10, font=('Arial', 13))
    startbutton2.grid(row=2, column=0)
    for widget in frame.winfo_children():
     widget.grid_configure(padx=10, pady=10)
    runonce =""



user_info_frame = tkinter.LabelFrame(frame, text="")
startnummerlabel = tkinter.Label(frame, text="", font=('Arial', 25), width=8)
startnummer2label = tkinter.Label(frame, text="", font=('Arial', 25), width=2)
roundnummerlabel = tkinter.Label(frame, text="", font=('Arial', 25), width=8)
roundnummerlabel2 = tkinter.Label(frame, text="", font=('Arial', 25), width=2)
startcompetition = tkinter.Button(frame, text="", width=20, height=10, font=('Arial', 25))
Stortplus = tkinter.Button(frame, text="", width=2, height=10, font=('Arial', 25))
Stortminus = tkinter.Button(frame, text="", width=2, height=10, font=('Arial', 25))
manresult = tkinter.Label(window,font=('Times', 80))
startnamn = tkinter.Label(frame, text="", font=('Arial', 25), width=15)
startnamn1 = tkinter.Label(frame, text="", font=('Arial', 25), width=15)
x = float(8.0)



window.mainloop()
