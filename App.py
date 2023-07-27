from tkinter import *
from tkinter import colorchooser

#Code for the main window (after next button is pressed)
def nextB():
    #Function for exiting the window
    def exit():
        mainWin.destroy()

    #Function for changing background color
    def bGround():
        mainWin.config(bg=colorchooser.askcolor()[1])

    #Main window
    mainWin = Tk()

    menuBar = Menu(mainWin, font=("Arial", 30)) #Main menu bar

    #File drop down menu
    fileMenu = Menu(menuBar, tearoff=0, font=("Arial", 10))
    menuBar.add_cascade(label="File", menu=fileMenu)
    fileMenu.add_command(label="New")
    fileMenu.add_command(label="Open")
    fileMenu.add_command(label="Save")
    fileMenu.add_command(label="Save As")
    fileMenu.add_command(label="Exit", command=exit)

    #Edit drop down menu
    editMenu = Menu(menuBar, tearoff=0, font=("Arial", 10))
    menuBar.add_cascade(label="Edit", menu=editMenu)
    editMenu.add_command(label="Background", command=bGround)
    editMenu.add_command(label="Font")
    editMenu.add_command(label="Font Size")

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