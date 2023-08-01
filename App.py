from tkinter import *
import tkinter as tk
from tkinter import colorchooser
from tkinter import filedialog
import calendar
import os

#Code for the main window (after next button is pressed)
def nextB():
    #Function for opening a new file
    def new():
        file = open("C:\\Users\\delll\\OneDrive\\Desktop\\MyApp\\file.txt", 'x')

    #Function for opening an already existing file
    def Open():
        os.startfile(filedialog.askopenfilename())

    #Function for exiting the window
    def exit():
        mainWin.destroy()

    #Function for changing background color
    def bGround():
        mainWin.config(bg=colorchooser.askcolor()[1])
    
    #Main window
    mainWin = Tk()

    menuBar = Menu(mainWin, font=("Arial", 30)) #Main menu bar
    i=10

    #File drop down menu
    fileMenu = Menu(menuBar, tearoff=0, font=("Arial", 10))
    menuBar.add_cascade(label="File", menu=fileMenu)
    fileMenu.add_command(label="New", command=new)
    fileMenu.add_command(label="Open", command=Open)
    fileMenu.add_command(label="Save")#, command=save)
    fileMenu.add_command(label="Save As")#, command=SaveAs)
    fileMenu.add_command(label="Exit", command=exit)

    #Edit drop down menu
    editMenu = Menu(menuBar, tearoff=0, font=("Arial", 10))
    menuBar.add_cascade(label="Edit", menu=editMenu)
    editMenu.add_command(label="Background", command=bGround)
    
    #Font Size menu in Edit Menu
    fsMenu = Menu(editMenu, tearoff=0, font=('Arial', 10))
    editMenu.add_cascade(label='Font Size', menu=fsMenu)
    while(i<=50):
        fsMenu.add_command(label=str(i))
        i+=2
    
    #Font menu in Edit Menu
    fontMenu = Menu(editMenu, tearoff=0, font=('Arial', 10))
    editMenu.add_cascade(label='Font', menu=fontMenu)
    fontMenu.add_command(label="Arial")
    fontMenu.add_command(label="Times New Roman")
    fontMenu.add_command(label="Calibri")

    #Entry box for title of project
    title = Entry(mainWin, font=('Arial', 30), width=20, bg='#0E9C7B')
    title.insert(0, 'Enter title')
    title.grid(row=1, column=2, columnspan=2, padx=(10, 10), pady=(10, 10))
    def clear_entry(event):
        title.delete(0, END)
    title.bind('<FocusIn>', clear_entry)

    #Account title label
    accLabel = Label(mainWin, text='Account title', font=('Arial', 20, 'bold'), bg='#FC4C4F')
    accLabel.grid(row=2, column=1)
    
    #Account title
    accTitle = Entry(mainWin, font=('Arial', 30), width=20, bg='#0E9C7B')
    accTitle.grid(row=2, column=2, columnspan=2, padx=(10, 10), pady=(10, 10))

    #Transaction Label
    transLabel = Label(mainWin, text='Choose Transaction', font=('Arial', 20, 'bold'), bg='#FC4C4F')
    transLabel.grid(row=3, column=1)

    #Frame to add the transactio menu
    #tFrame = Frame(mainWin, width=200, height=50)
    #tFrame.grid(row=3, column=2)
    
    #Transaction Menu
    tMenu = Menu(mainWin, font=('Arial', 20))  # Example: Create a Transaction menu, add commands, and associate with the mainWin window.
    tMenu.add_command(label="Transaction 1")
    tMenu.add_command(label="Transaction 2")
    tMenu.add_command(label="Transaction 3")
    
    cFrame = Frame(mainWin, width=200, height=200)
    cFrame.grid(row=2, column=4, rowspan=3, columnspan=2)
    
    #Button to show preview
    preview = Button(mainWin, text='Show Preview', font=('Arial', 15), bg='black', fg='#FC4C4F')
    preview.place(relx=0.98, rely=0.98, anchor='se')

    mainWin.geometry("900x600")
    mainWin.config(background="#FC4C4F", menu=menuBar)
    welcome.destroy()

#Welcome window
welcome = Tk()

label1 = Label(welcome, text="My App", font=('Arial',50,'bold'),bg='#FC4C4F')
label2 = Label(welcome, text="WELCOME", font=('Arial',50),bg='#FC4C4F')
nextButton = Button(text='NEXT', font=('Arial',40), bg='black', fg='#FC4C4F', command=nextB)

label1.pack()   
label2.pack()
nextButton.place(relx=0.35, rely=0.6)
welcome.geometry("500x500")
welcome.config(background="#FC4C4F")

welcome.mainloop()