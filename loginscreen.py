import tkinter as tk
import dahboard
#from pyrebase import pyrebase


label1=None
root=tk.Tk()
 
# setting the windows size
root.geometry("600x400")
  
# declaring string variable
# for storing name and password
name_var=tk.StringVar()
passw_var=tk.StringVar()
"""""
Config = {
    "apiKey": "AIzaSyB6ANKP9lTPrIEgBjjEoW4Bim1fXv-F4Sk",
    "authDomain": "tkinter-49677.firebaseapp.com",
    "databaseURL": "https://tkinter-49677-default-rtdb.firebaseio.com",
    "projectId": "tkinter-49677",
    "storageBucket": "tkinter-49677.appspot.com",
    "messagingSenderId": "1071856241582",
    "appId": "1:1071856241582:web:d37d9c6a8b99a20585d63f"
  }

firebase=pyrebase.initialize_app(Config)
auth=firebase.auth()
db=firebase.database()
 """""
# defining a function that will
# get the name and password and
# print them on the screen
def submit():
 
    name=name_var.get()
    password=passw_var.get()
    global label1
    print("The name is : " + name)
    print("The password is : " + password)
     
    name_var.set("")
    passw_var.set("")
    flag=0

    #try:
        #login = auth.sign_in_with_email_and_password(name, password)
    print('harsh')
    if(name=='admin'):
        print("Successfully logged in!")
        flag=1
        root.destroy()
        # print(auth.get_account_info(login['idToken']))
       # email = auth.get_account_info(login['idToken'])['users'][0]['email']
       # print(email)
    #except:
    else:
        label1.configure(text='Invalid User ID or Password')
        label1.config(bg= "gray51", fg= "white")
    print(flag)
    return flag
     
def login():   
    # creating a label for
    # name using widget Label
    name_label = tk.Label(root, text = 'Username', font=('calibre',10, 'bold'))
    
    # creating a entry for input
    # name using widget Entry
    name_entry = tk.Entry(root,textvariable = name_var, font=('calibre',10,'normal'))
    
    # creating a label for password
    passw_label = tk.Label(root, text = 'Password', font = ('calibre',10,'bold'))
    
    # creating a entry for password
    passw_entry=tk.Entry(root, textvariable = passw_var, font = ('calibre',10,'normal'), show = '*')
    global label1
    # creating a button using the widget
    # Button that will call the submit function
    sub_btn=tk.Button(root,text = 'Submit', command = submit)
    label1 = tk.Label(root, text = '', font=('calibre',10, 'bold'))
    
    # placing the label and entry in
    # the required position using grid
    # method
    '''
    name_label.grid(row=0,column=0)
    name_entry.grid(row=0,column=1)
    passw_label.grid(row=1,column=0)
    passw_entry.grid(row=1,column=1)
    sub_btn.grid(row=2,column=1)
'''
    name_label.pack()
    name_entry.pack()
    passw_label.pack()
    passw_entry.pack()
    sub_btn.pack()
    label1.pack()

    # performing an infinite loop
    # for the window to display
    root.mainloop()
