#class dashboard(object):
 #   def meth():
  #      print("class dash")
from logging import PlaceHolder
import tkinter as tk
from tkinter import *
from tkinter import filedialog
from tkinter.filedialog import askopenfile
from PIL import Image, ImageTk
def kills(my_w):
    my_w.destroy()
def upload_file():
    my_w = tk.Tk()
    my_w.geometry("410x300")  # Size of the window 
    my_w.title('Gods EYE')
    name_var=tk.StringVar()
    name=name_var.get()
    my_font1=('times', 18, 'bold')
    l1 = tk.Label(my_w,text='Upload Files & display',width=30,font=my_font1)  
    l1.grid(row=1,column=1,columnspan=4)
    b1 = tk.Button(my_w, text='Upload Files', 
    width=20,command = lambda:kills(my_w))
    b1.grid(row=2,column=1,columnspan=4)
    # creating a label for
# name using widget Label
    name_label = tk.Label(my_w, text = 'Name', font=('calibre',10, 'bold'))
  
# creating a entry for input
# name using widget Entry
    
    
    f_types = [('Jpg Files', '*.jpg'),
    ('PNG Files','*.png')]   # type of files to select 
    filename = tk.filedialog.askopenfilename(multiple=True,filetypes=f_types)
    
    col=1 # start from column 1
    row=3 # start from row 3 
    for f in filename:
        img=Image.open(f) # read the image file
        
        img=img.resize((100,100)) # new width & height
        img=ImageTk.PhotoImage(img)
        e1 =tk.Label(my_w)
        e1.grid(row=row,column=col)
        e1.image = img
        e1['image']=img # garbage collection 
        if(col==3): # start new line after third column
            row=row+1# start wtih next row
            col=1    # start with first column
        else:       # within the same row 
            col=col+1 # increase to next column                 
    my_w.mainloop()  # Keep the window open
    print(name)
    return filename

