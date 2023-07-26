from tkinter import *

def next():
    mainWin = Tk()

    menuBar = Menu(mainWin, font=("Arial", 30))

    fileMenu = Menu(menuBar, tearoff=0, font=("Arial", 10))
    menuBar.add_cascade(label="File", menu=fileMenu)
    fileMenu.add_command(label="New")
    fileMenu.add_command(label="Open")
    fileMenu.add_command(label="Save")
    fileMenu.add_command(label="Save As")
    fileMenu.add_command(label="Exit")

    editMenu = Menu(menuBar, tearoff=0, font=("Arial", 10))
    menuBar.add_cascade(label="Edit", menu=editMenu)
    editMenu.add_command(label="Background")
    editMenu.add_command(label="Font")
    editMenu.add_command(label="Font Size")

    mainWin.geometry("900x600")
    mainWin.config(background="#FC4C4F", menu=menuBar)
    welcome.destroy()

welcome = Tk()

label1 = Label(welcome, text="My App", font=('Arial',50,'bold'),bg='#FC4C4F')
label2 = Label(welcome, text="WELCOME", font=('Arial',50),bg='#FC4C4F')
next = Button(text='NEXT', font=('Arial',40), bg='black', fg='#FC4C4F', command=next)

label1.pack()   
label2.pack()
next.place(x=150, y=300)
welcome.geometry("500x500")
welcome.config(background="#FC4C4F")

welcome.mainloop()