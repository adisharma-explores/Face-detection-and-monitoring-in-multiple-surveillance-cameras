#Import the required Libraries
from tkinter import *
from tkinter import ttk

#Create an instance of Tkinter frame
entry=None
win=None
string=""
def display_text():
    print("hj")
    global entry
    global string
    global win
    string= entry.get()
    win.destroy()
    print(string)
def nam():
    global win
    win=Tk()
    global entry
    #Set the geometry of Tkinter frame
    win.geometry("750x250")
    #Initialize a Label to display the User Input
    label=Label(win, text="Name")
    label.pack()
    
    #Create an Entry widget to accept User Input
    entry= Entry(win, width= 40)
    entry.focus_set()
    entry.pack()
    global string
    #Create a Button to validate Entry Widget
    ttk.Button(win, text= "Okay",width= 20, command=display_text).pack(pady=20)
    win.mainloop()
    return string
