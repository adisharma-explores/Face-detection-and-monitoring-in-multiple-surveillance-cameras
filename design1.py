import tkinter as tk
import customtkinter
import sys
def kills(my_w):
    my_w.destroy()
def logg():
    my_w = tk.Tk()
    my_w.geometry("810x700")  # Size of the window 
    my_w.title('Gods EYE')
    # create label on CTkToplevel window
    
    with open('log1.txt') as f:
        lines = f.readlines()
        print(len(lines))
    for r in lines:
        print(len(r))
        if len(r)!=0:
            label = tk.Label(my_w,text=r)  
            label.pack()
    b1 = tk.Button(my_w, text='Exit', 
    width=20,command = lambda:kills(my_w))
    b1.pack()
    my_w.mainloop()

