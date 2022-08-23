from tkinter import *
from tkinter import ttk
from tkinter import simpledialog
from tkinter import Entry
#Create an instance of Tkinter frame
win=None
arr=[]
arrf=[]
arrfi=[]
#Set the geometry of Tkinter frame

entry=None
def display_text(n):
    global win
    global entry
    string= entry.get()
    n=int(string)
    n1=0

    while n1<n:
        USER_INP = simpledialog.askstring(title="IP",
                                  prompt="Enter the ip address:")
        GRAPH_INP = simpledialog.askstring(title="IP",
                                  prompt="Enter the connected cameras :")
        arr1=GRAPH_INP.split(",")
        arrfi = [int(numeric_string) for numeric_string in arr1]
        arrf.append(arrfi)
        arr.append(USER_INP)
        n1 += 1
    win.destroy()
    

#Initialize a Label to display the User Input
def ipadda():
    global win
    win= Tk()
    win.geometry("750x250")
    iparr=[]
    global entry
    label=Label(win, text="", font=("Courier 22 bold"))
    label.pack()
    Label(win, text="Camera IP input",font=("Arial", 14)).pack()
    Label(win, text="").pack()
    Label(win, text="Enter the Number of cameras:",font=("Arial", 10)).pack()
    #Create an Entry widget to accept User Input
    entry= Entry(win, width= 40)
    entry.focus_set()
    entry.pack()
    
    #Create a Button to validate Entry Widget
    ttk.Button(win, text= "Submit",width= 20, command= lambda: display_text(2)).pack(pady=20)
    win.mainloop()
    arrt=arr+arrf
    arrs=' '.join([str(elem) for elem in arrt])
    with open('addr.txt', 'w') as f:
        f.write(arrs)
    return arr,arrf


