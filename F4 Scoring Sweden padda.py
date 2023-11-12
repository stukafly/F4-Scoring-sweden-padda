import tkinter
from tkinter import ttk
from tkinter import messagebox
import sqlite3



def judges_data():

    # Create Table
        conn = sqlite3.connect('F4scoring.db')



        table_create_query = '''CREATE TABLE IF NOT EXISTS judge_Data 
                    (IDnr int key, judge TEXT, judgenr INT, pilot TEXT, startnr INT, R1M1 INT, R1M2 INT, 
                    R1M3 INT, R1M4 INT, R1M5 INT, R1M6 INT, R1M7 INT, R1M8 INT, R1M9 INT, R1M10 INT, R1M11 INT, 
                    R1M12 INT, R1M13 INT, R1MT1 TEXT, R1MT2 TEXT, R1MT3 TEXT, R1MT4 TEXT, R1MT5 TEXT, R1MT6 TEXT,
                    R1MT7 TEXT, R1MT8 TEXT, R1MT9 TEXT, R1MT10 TEXT, R1MT11 TEXT, R1MT12 TEXT, R1MT13 TEXT,
                    R2M1 INT, R2M2 INT, 
                    R2M3 INT, R2M4 INT, R2M5 INT, R2M6 INT, R2M7 INT, R2M8 INT, R2M9 INT, R2M10 INT, R2M11 INT, 
                    R2M12 INT, R2M13 INT, R2MT1 TEXT, R2MT2 TEXT, R2MT3 TEXT, R2MT4 TEXT, R2MT5 TEXT, R2MT6 TEXT,
                    R2MT7 TEXT, R2MT8 TEXT, R2MT9 TEXT, R2MT10 TEXT, R2MT11 TEXT, R2MT12 TEXT, R2MT13 TEXT,
                    R3M1 INT, R3M2 INT, 
                    R3M3 INT, R3M4 INT, R3M5 INT, R3M6 INT, R3M7 INT, R3M8 INT, R3M9 INT, R3M10 INT, R3M11 INT, 
                    R3M12 INT, R3M13 INT, R3MT1 TEXT, R3MT2 TEXT, R3MT3 TEXT, R3MT4 TEXT, R3MT5 TEXT, R3MT6 TEXT,
                    R3MT7 TEXT, R3MT8 TEXT, R3MT9 TEXT, R3MT10 TEXT, R3MT11 TEXT, R3MT12 TEXT, R3MT13 TEXT)
            '''
        conn.execute(table_create_query)
        c = conn.cursor()


        c.execute('DELETE FROM judge_Data;', )
        # Insert Data
        data_insert_query = '''INSERT INTO judge_Data (IDnr , judge, judgenr, 
            pilot, startnr, R1MT1, R1MT2, R1MT3, R1MT4, R1MT5, R1MT6, R1MT7, R1MT8, R1MT9, R1MT10, R1MT11, R1MT12, R1MT13) VALUES 
            (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)'''
        data_insert_tuple = (1, "BÖRJE", 2,
                                 "otto", 1, "start", "loop", "liggande åtta", "roll", "kubansk åtta", "wingover", "under 6 M",
                                 "sjunkande cirkel","touch and go", "landning", "ljud", "jämnhet", "hastighet")

        c.execute(data_insert_query, data_insert_tuple)


        conn.commit()
        conn.close()


        user_info_frame.config(text="Put in Judge Nr and name")
        user_info_frame.grid(row=0, column=0, padx=20, pady=10)


        radio_var = tkinter.StringVar(value="1")


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
     startnummer2label.config(text=str(startnummerval))
     startnummer2label.grid(row=0, column=1)
     roundnummerlabel.config(text="Round Nr:")
     roundnummerlabel.grid(row=1, column=0)
     roundnummerlabel2.config(text=str(roundnr))
     roundnummerlabel2.grid(row=1, column=1)
     startcompetition.config(text="start Round", command=judgepoint)
     startcompetition.grid(row=2, column=2)

     try:
         global numberofcompetitors


         connection = sqlite3.connect('F4scoring.db')
         cursor = connection.cursor()

         numberofcompetitors_query = """SELECT COUNT(pilot) from judge_data"""
         cursor.execute(numberofcompetitors_query)
         numberofcompetitors = cursor.fetchone()[0]
         cursor.close()

     except sqlite3.Error as error:

         tkinter.messagebox.showwarning(title="Error", message="hittar inte databas")
     finally:
         if connection:
             connection.close()


def judgepoint():
    try:
        global manval
        global startnummerval


        connection = sqlite3.connect('F4scoring.db')
        cursor = connection.cursor()

        sqlite_select_query = """SELECT * from judge_data"""
        cursor.execute(sqlite_select_query)
        records = cursor.fetchmany(int(startnummerval))

        for row in records:
            pilot = (row[3])
            manover = (row[manval])


        cursor.close()

    except sqlite3.Error as error:

        tkinter.messagebox.showwarning(title="Error", message="hittar inte databas")
    finally:
        if connection:
            connection.close()


    startnummerlabel.grid_forget()
    startnummer2label.grid_forget()
    roundnummerlabel.grid_forget()
    roundnummerlabel2.grid_forget()
    startcompetition.grid_forget()



    Stortminus.config (font=('Times', 48))
    Stortminus ["bg"] = "#fb5050"
    Stortminus["fg"] = "#000000"
    Stortminus ["justify"] = "center"
    Stortminus ["text"] = "-"
    Stortminus .place(x=0, y=110, width=300, height=314)
    Stortminus ["command"] = spinminus


    manresult.config (text= str(x), font=('Times', 100))
    manresult["borderwidth"] = "1px"
    manresult["fg"] = "#333333"
    manresult["justify"] = "center"
    manresult.place(x=320, y=110, width=300, height=314)

    Stortplus.config(font=('Times', 48))
    Stortplus["bg"] = "#87fb3a"
    Stortplus["fg"] = "#000000"
    Stortplus["justify"] = "center"
    Stortplus["text"] = "+"
    Stortplus.place(x=630, y=110, width=300, height=314)
    Stortplus["command"] = spinplus

    Next1.config (font=('Times', 48))
    Next1["bg"] = "#87fb3a"
    Next1["fg"] = "#000000"
    Next1["justify"] = "center"
    Next1["text"] = "Next"
    Next1.place(x=370, y=420, width=180, height=180)
    Next1["command"] = nextmanover

    GLabel_247.config(font=('Times', 18))
    GLabel_247["fg"] = "#333333"
    GLabel_247["justify"] = "center"
    GLabel_247["text"] = "pilot:"
    GLabel_247.place(x=100, y=20, width=200, height=25)

    startnamn2.config(font=('Times', 18))
    startnamn2["fg"] = "#333333"
    startnamn2["justify"] = "left"
    startnamn2["text"] = pilot
    startnamn2.place(x=100, y=50, width=200, height=25)

    GLabel_2.config(font=('Times', 18))
    GLabel_2["fg"] = "#333333"
    GLabel_2["justify"] = "center"
    GLabel_2["text"] = "Manöver:"
    GLabel_2.place(x=350, y=20, width=200, height=25)

    GLabel_437.config(font=('Times', 18), justify="center")
    GLabel_437["fg"] = "#333333"
    GLabel_437["text"] = manover
    GLabel_437.place(x=350, y=40, width=200, height=30)



def spinplus():
    global x
    if x<=9.5:
     x +=0.5
     manresult.config(text=str(x), font=('Times', 100))






def spinminus  ():
    global x
    if x >= 0.5:
        x -= 0.5
        manresult.config(text=str(x), font=('Times', 100))

def nextmanover():
    global manval
    global x
    global startnummerval
    global roundnr
    global newround

    manval1 = manval - newround
    man = manval1 - 17
    st = str(startnummerval)
    cell = str("R"+str(roundnr)+"M"+str(man))
    conn = sqlite3.connect('F4scoring.db')
    c = conn.cursor()
    c.execute('''UPDATE judge_Data SET  {0}  = (?) WHERE startnr = {1} '''.format(cell,st),[str(x)])
    conn.commit()
    conn.close()
    manval += 1


    if man <= 12:
        judgepoint()
    else:
        nextstart()

def nextstart():
    global manval
    global startnummerval
    global roundnr
    global newround
    Stortplus.place_forget()
    Stortminus.place_forget()
    manresult.place_forget()
    Next1.place_forget()
    startnamn2.place_forget()
    GLabel_247.place_forget()
    GLabel_2.place_forget()
    GLabel_437.place_forget()

    manval = 18 + newround
    startnummerval += 1

    if startnummerval > numberofcompetitors:
       nyrunda()
    else:
        startnummer()

def slut():
    window.title("tävling slut")

def nyrunda():
    global startnummerval
    global roundnr
    global newround
    global manval
    roundnr += 1
    startnummerval = 1
    newround += 26
    manval = 18 + newround
    if roundnr > 3:
        slut()
    else:
        startnummer()


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
Stortplus = tkinter.Button(window, text="", width=2, height=10, font=('Arial', 25))
Stortminus = tkinter.Button(window, text="", width=2, height=10, font=('Arial', 25))
manresult = tkinter.Label(window,font=('Times', 80))
startnamn = tkinter.Label(frame, text="", font=('Arial', 25), width=15)
startnamn1 = tkinter.Label(frame, text="", font=('Arial', 25), width=15)
Next1 = tkinter.Button(window, text="", width=2, height=10, font=('Arial', 25))
startnamn2 = tkinter.Label(window, text="", font=('Arial', 25), width=15)
GLabel_247 = tkinter.Label(window, font=('Times', 18))
GLabel_2 = tkinter.Label(window, font=('Times', 18))
GLabel_437 = tkinter.Label(window, font=('Times', 18), justify="center")
numberofcompetitors = 1
manval = 18
x = float(8.0)
startnummerval = 1
roundnr = 1
newround = 0


window.mainloop()
