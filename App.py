from tkinter import *
from tkinter import colorchooser
from tkinter import filedialog
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

    #Entry box for title
    title = Entry(mainWin, font=('Arial', 40), width=20)
    title.insert(0, 'Enter title')
    title.pack()

    mainWin.geometry("900x600")
    mainWin.config(background="#FC4C4F", menu=menuBar)
    welcome.destroy()
    mainWin.mainloop()

#Welcome window
welcome = Tk()

label1 = Label(welcome, text="My App", font=('Arial',50,'bold'),bg='#FC4C4F')
label2 = Label(welcome, text="WELCOME", font=('Arial',50),bg='#FC4C4F')
nextB = Button(text='NEXT', font=('Arial',40), bg='black', fg='#FC4C4F', command=nextB)

label1.pack()   
label2.pack()
nextB.place(x=150, y=300)
welcome.geometry("500x500")
welcome.config(background="#FC4C4F")

welcome.mainloop()